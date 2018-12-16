from django.urls import path
from .views import home, autore_detail, AutoreDetailViewCB
#Qui vengono definiti i vari path delle fuzioni o classi definite nel file views.py
urlpatterns = [
    path("", home, name="homeview"),
    path("autore/<int:pk>", AutoreDetailViewCB.as_view(), name="autore_detail")
]
