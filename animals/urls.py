from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('dogs', views.dogs, name='dogs'),
    path('cats', views.cats, name='cats'),
    path('contact', views.contact, name='contact')
]