from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic

# Create your views here.


class ListaLibros(generic.ListView):
    model = Book


class DetalleLibros(generic.DetailView):
    model = Book


def index(request):
    num_book = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_author = Author.objects.all().count()
    libros_disponibles = BookInstance.objects.filter(status__exact='a').count()
    return render(request, 'index.html',
                  {'num_book': num_book,
                   'num_instances': num_instances,
                   'num_author': num_author,
                   'libros_disponibles': libros_disponibles})


def libros(request):
    return render(request, 'libros.html')


def autores(request):
    return render(request, 'autores.html')


def generos(request):
    return render(request, 'generos.html')
