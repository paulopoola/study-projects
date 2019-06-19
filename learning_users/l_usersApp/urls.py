from django.urls import path,include
from l_usersApp import views

app_name = 'l_usersApp'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
]
