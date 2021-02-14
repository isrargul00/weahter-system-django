from django.urls import path
from .views import home,weather
app_name = 'core'

urlpatterns =[
    path('',home,name="home"),
    path('weather',weather,name="weather"),
]