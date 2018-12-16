from django.db import models
from django.urls import reverse

""" Classe che identifica un Autore. Gli attributi sono: nome, cognome e nazione. Attraverso la funzione
.libro_set.all() si puà accedere a tutti i libri dell'autore."""
class Autore(models.Model):
    nome = models.CharField(max_length = 25)
    cognome = models.CharField(max_length = 25)
    nazione = models.CharField(max_length = 25)

    def __str__(self):
        return self.nome + " " + self.cognome

    def get_absolute_url(self):
        return reverse("autore_detail", kwargs={"pk":self.pk})

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"




""" Classe che identifica un genere di libro. Un libro può avere più genere, la relazione è molti a molti. """
class Genere(models.Model):
    nome = models.CharField(max_length = 25)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"




""" La classe libro, oltre agli attributi titolo e isbn, contiene due chiavi esterni a Genere (Molti a molti) e Autore (Foreign key). """
class Libro(models.Model):
    titolo = models.CharField(max_length = 25)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE)
    genere = models.ManyToManyField(Genere)
    isbn = models.CharField(max_length = 25)

    def __str__(self):
        return self.titolo + ", " + self.isbn

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"
