from django.contrib import admin

# Register your models here.

from .models import Autore, Genere, Libro

# Usato per gestire i modelli dalla console di django
admin.site.register(Autore)
admin.site.register(Genere)
admin.site.register(Libro)
