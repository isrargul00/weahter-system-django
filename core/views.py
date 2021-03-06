from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from django.http import HttpResponse
# Create your views here.

def home(request):
    context={}
    return render(request,'core/home.html',context)



def weather(request):
    #url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=5d82bd007e89d3d09e87df9f526cd725'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=5d82bd007e89d3d09e87df9f526cd725'
    city = request.GET.get('city')
    city_weather = requests.get(url.format(city)).json()

    print(city_weather['main']['temp'])


    #request the API data and convert the JSON to Python data types
    data = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    return JsonResponse(data)


@login_required
def logoutview(request):
    logout(request)
    return redirect('core:home')