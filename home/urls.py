from django.contrib import admin
from django.urls import path,include
from home import views



urlpatterns = [
    
    path('',views.login, name="login"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('create_account', views.createAccount, name="create_account"),
    path('home', views.home, name='home'),
    path('collegeDetails', views.collegeDetails,name='collegeDetails'),
    path('delete', views.delete, name="delete"),
    path('fetch',views.fetch, name="fetch"),
    path('update_details',views.update, name="update"),
    path('search',views.search, name="search")
    
]