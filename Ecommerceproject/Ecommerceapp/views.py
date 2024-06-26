from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
# def index(request):
#     return HttpResponse("i am here")



def allprocat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=Products.objects.filter(category=c_page,available=True)
    else:
        products_list=Products.objects.all().filter(available=True)
    paginator=Paginator(products_list,8)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':c_page,'products':products})


def prodetail(request,c_slug,products_slug):
    try:
        products=Products.objects.get(category__slug=c_slug,slug=products_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'products':products})
