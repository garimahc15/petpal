from django.db import models

# Create your models here.

class CatandDog(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to= 'pics')
    desc= models.TextField()

class Catsforall(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to= 'pics')

class Dogsforall(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to= 'pics')

class Newsletter(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=200)

class ContactForm(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
    subject= models.CharField(max_length= 200)
    message= models.TextField()