

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, Movie
from .forms import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

def index(request):
    allmovies = Movie.objects.select_related('user').all()
    return render(request,'index.html',{'allmovies':allmovies})

def details(request,movieid):
    movie = get_object_or_404(Movie, pk=movieid)
    return render(request,'details.html',{'movie':movie})

@login_required
def add_movie(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        languages = request.POST.get('languages')
        actors = request.POST.get('actors')
        year = request.POST.get('year')
        link = request.POST.get('link')
        rating = request.POST.get('rating')


        if request.user.is_authenticated:
            movie = Movie(
                title=title,
                description=description,
                image=image,
                category=category,
                languages=languages,
                actors=actors,
                year=year,
                link=link,
                rating=rating,
                user=request.user
            )
            movie.save()
            messages.info(request, "Movie successfully added")
            return redirect("Movieapp:user_profile")
        else:
            messages.error(request, "You must be logged in to add a movie")
            return redirect("Movieapp:login")

    return render(request, 'addmovies.html')




@login_required
def update_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = MovieUpdateForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('Movieapp:user_profile')
    return render(request, 'update_movie.html', {'form': form, 'movie': movie})
@login_required
def delete(request,id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        movie.delete()
        return redirect('Movieapp:user_profile')
    return render(request,'delete.html',{"movie":movie})

@login_required
def user_profile(request):
    current_user = request.user
    user_movies = Movie.objects.filter(user=current_user)
    return render(request, 'profile.html', {'allmovies': user_movies, 'user': current_user})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request,"User created successfully")
            auth.login(request, user)
            return redirect('Movieapp:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session.set_expiry(86400)
            return redirect('Movieapp:user_profile')
        else:
            messages.info(request,"invalid credentails")
            return redirect("Movieapp:login")
    return render(request,"login.html")
@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")
@login_required
def update_user(request, id):
    user = get_object_or_404(CustomUser, id=id)
    form = CustomUserUpdateForm(request.POST or None, request.FILES or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('Movieapp:user_profile')
    return render(request, 'update_user.html', {'form': form, 'user': user})
@login_required
def user_details(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    movies = Movie.objects.filter(user=user)
    return render(request,'user_details.html', {'user': user, 'movies': movies})







def Searchresults(request):
    query = request.GET.get('q', '')
    movie_list = Movie.objects.all()

    if query:
        movie_list = movie_list.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Pagination setup
    paginator = Paginator(movie_list, 10)  # Show 10 movies per page
    page_number = request.GET.get('page')

    try:
        movies = paginator.page(page_number)
    except PageNotAnInteger:

        movies = paginator.page(1)
    except EmptyPage:

        movies = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'query': query, 'movies': movies})



