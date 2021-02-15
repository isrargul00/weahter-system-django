from django.urls import path
from .views import home,weather,logoutview
app_name = 'core'

urlpatterns =[
    path('',home,name="home"),
    path('weather',weather,name="weather"),
    path('logout',logoutview,name='logout'),
]