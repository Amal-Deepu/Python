from django.contrib import admin
from django.urls import path,include

from . import views
app_name='Ecommerceapp'

urlpatterns = [

    path('',views.allprocat,name='allprocat'),
    path('<slug:c_slug>/',views.allprocat,name='products_by_category'),
    path('<slug:c_slug>/<slug:products_slug>/', views.prodetail, name='productCatdetail')
]