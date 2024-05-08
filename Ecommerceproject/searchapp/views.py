from django.shortcuts import render

# Create your views here.
from Ecommerceapp.models import Products
from django.db.models import Q
def Searchresults(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Products.objects.filter(Q(name__contains=query) | Q(description__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})

