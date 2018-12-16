from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Autore, Genere, Libro

""" Qui vengono definite le varie viste. La funzione autore_detail e la classe AutoreDetailViewCB sono due modi diversi per passare ad un template la stessa """
def home(request):
    autori = Autore.objects.all()
    generi = Genere.objects.all()
    libri = Libro.objects.all()
    context = {"autori": autori, "generi":generi, "libri":libri}
    return render(request, "homepage.html", context)

def autore_detail(request, pk):
    autore = Autore.objects.get(id=pk)
    libri = Libro.objects.filter(autore=pk)
    context = {"autore": autore, "libri": libri}
    return render(request, "autore_detail.html", context)

class AutoreDetailViewCB(DetailView):
    model = Autore
    template_name = "autore_detail.html"
