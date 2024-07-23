
from django.urls import path

from Movieapp import views
app_name='Movieapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:movieid>/', views.details, name='details'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('update_movie/<int:id>/', views.update_movie, name='update_movie'),
    path('delete_movie/<int:id>/', views.delete, name='delete_movie'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('user/<int:user_id>/', views.user_details, name='user_details'),
    path('search/', views.Searchresults, name='search'),

]
