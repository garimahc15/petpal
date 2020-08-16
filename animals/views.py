from django.shortcuts import render
from .models import CatandDog  # catdog class for homepage general image display. will have different pages and classes for cats and dogs
# Create your views here.


def index(request):
    catdogs= CatandDog.objects.all()
    return render(request, 'index.html', {'catdogs': catdogs})