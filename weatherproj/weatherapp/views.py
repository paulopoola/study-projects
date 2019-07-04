import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=42a7d91768b73aec49a81694070b3be1'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                response = requests.get(url.format(new_city)).json()

                if response['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exist!'
            else:
                err_msg = 'City already exists in the database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        response = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name.capitalize(),
            'temperature' : response['main']['temp'],
            'humidity':response['main']['humidity'],
            'wind_speed':response['wind']['speed'],
            'description' : response['weather'][0]['description'],
            'icon' : response['weather'][0]['icon'],
            'in_Fahrenhiet' : int((response['main']['temp'])*(1.8) + 32)
        }
        weather_data.append(city_weather)


    context = {
        'weather_data' : weather_data,
        'form' : form,
        'message' : message,
        'message_class' : message_class,
    }

    return render(request, 'weatherapp/weather.html', context)

def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')
