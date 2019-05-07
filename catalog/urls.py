from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('libros', views.ListaLibros.as_view(), name='libros'),
               path('libros/<pk>', views.DetalleLibros.as_view(), name='book-detail'),
               path('autores', views.autores, name='autores'),
               path('generos', views.generos, name='generos'),

               ]
