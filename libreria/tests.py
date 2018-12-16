from django.test import TestCase
from .models import Autore, Genere, Libro

# Semplice test per l'autore
class AutoreTestCase(TestCase):
    def setUp(self):
        Autore.objects.create(nome="Dante", cognome="Alighieri", nazione="Italia")

    def test_string_autore(self):
        dante = Autore.objects.get(id=1)
        self.assertEqual(dante.__str__(), "Dante Alighieri")
