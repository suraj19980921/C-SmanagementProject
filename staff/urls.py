from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    
    path('staffinfo', views.staff,name='staff'),
    path('staffDetails', views.staffDetails,name='staffDetails'),
    path('delete', views.delete, name="delete"),
    path('fetchStaff',views.fetch, name="fetch"),
    path('update_details',views.update, name="update"),
    path('search',views.search, name="search")
    
]