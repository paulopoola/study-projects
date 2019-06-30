# Groups urls.py
from django.urls import path
from . import views

app_name ='communities'

#re_path(r'^(?P<pk>[-\w]+)/$' old syntax replaced by path('<slug:pk>'),
#and url(r'^(?P<pk>\d+)/$') old replaced with path('<int:pk>/'

urlpatterns =[
    path('', views.ListCommunities.as_view(), name='all'),
    path('new/', views.CreateCommunity.as_view(), name='create'),
    path('posts/in/<slug:pk>/', views.SingleCommunity.as_view(), name= 'single'),
    path('join/<slug:pk>/', views.JoinCommunity.as_view(), name='join'),
    path('leave/<slug:pk>/', views.LeaveCommunity.as_view(), name='leave'),
]
