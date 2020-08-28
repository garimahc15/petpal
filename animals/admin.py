from django.contrib import admin
from .models import CatandDog, Catsforall, Dogsforall, Newsletter, ContactForm
# Register your models here.

admin.site.register(CatandDog)
admin.site.register(Catsforall)
admin.site.register(Dogsforall)
admin.site.register(Newsletter)
admin.site.register(ContactForm)