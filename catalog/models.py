from django.db import models
from django.urls import reverse
import uuid
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30, help_text="Nombre de Autor")
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


class Genre(models.Model):
    name = models.CharField(max_length=30, help_text="Nombre de Genero")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30, help_text="Idioma")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30, help_text="Titulo del Libro")
    summary = models.TextField(max_length=40, help_text="Resumen del Libro")
    imprint = models.CharField(max_length=20)
    isbn = models.CharField('ISBN', max_length=13)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="ID Unico de libro")
    due_back = models.DateField()
    LOAN_STATUS = (('m', 'Maintenance'), ('o', 'On loan'),
                   ('a', 'Available'), ('r', 'Reserved'))
    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='m',
                              help_text='Disponibilidad del Libro')

    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)
