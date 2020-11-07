from django.urls import path
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('homepage_2/', views.homepage_2, name='homepage_2'),
    path('category/', views.category, name='category'),

]
