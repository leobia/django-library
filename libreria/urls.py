from django.urls import path
from .views import home, autore_detail, AutoreDetailViewCB, index
#Qui vengono definiti i vari path delle fuzioni o classi definite nel file views.py
urlpatterns = [
    path("libri", home, name="homeview"),
    path("autore/<int:pk>", AutoreDetailViewCB.as_view(), name="autore_detail"),
    path("index", index, name="indexView")
]
