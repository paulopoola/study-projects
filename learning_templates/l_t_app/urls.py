from django.urls import path
from l_t_app import views

#TEMPLATE TAGGING
app_name = 'l_t_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name = 'other')

]
