from django.shortcuts import render, redirect
from .models import CatandDog, Catsforall, Dogsforall, Newsletter, ContactForm  # catdog class for homepage general image display. will have different pages and classes for cats and dogs
from django.http import HttpResponseRedirect
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

def search(request):
    if request.method == 'POST':
        pettype = request.POST['pettype']
        if pettype in ["Dogs", "dogs", "dog", "Dog"]:
            dogs= Dogsforall.objects.all()
            return render(request, 'dogs.html', {'dogs': dogs})
        elif pettype in ["Cats", "cats", "Cat", "cat"]:
            cats= Catsforall.objects.all()
            return render(request, 'cats.html', {'cats': cats})
    else:
        return render(request, 'index.html')

def subscribe(request):
    if request.method== 'POST':
        name= request.POST['name']
        email= request.POST['email']

        if Newsletter.objects.filter(name= name, email= email).exists()==False:  #if the user doesn't already exist then make a new entry in database
            user= Newsletter(name= name, email= email)
            user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   #this is done to return to same page that the user was before submitting the form
    else:
        return render(request, 'index.html')

def message(request):
    if request.method== 'POST':
        name= request.POST['name']
        email= request.POST['email']
        subject= request.POST['subject']
        message= request.POST['message']

        user= ContactForm(name=name, email=email, subject=subject, message=message)
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'index.html')

