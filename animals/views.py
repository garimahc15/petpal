from django.shortcuts import render
from .models import CatandDog, Catsforall, Dogsforall  # catdog class for homepage general image display. will have different pages and classes for cats and dogs
# Create your views here.


def index(request):
    catdogs= CatandDog.objects.all()
    return render(request, 'index.html', {'catdogs': catdogs})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cats(request):
    cats= Catsforall.objects.all()
    return render(request, 'cats.html', {'cats': cats})

def dogs(request):
    dogs= Dogsforall.objects.all()
    return render(request, 'dogs.html', {'dogs': dogs})