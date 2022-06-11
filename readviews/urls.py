from django.urls import path
from readviews import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index_series/', views.index_series, name="index_series"),
    path('index_peliculas', views.index_peliculas, name="index_peliculas"),
    path('index_libros', views.index_libros, name="index_libros"),
    path('agregar_serie/', views.agregar_serie, name="agregar_serie"),
    path('agregar_pelicula/', views.agregar_pelicula, name="agregar_pelicula"),
    path('agregar_libro/', views.agregar_libro, name="agregar_libro"),
    path('borrar_serie/<identificador>', views.borrar_serie, name="borrar_serie"),
    path('agregar_pelicula/', views.agregar_pelicula, name="agregar_pelicula"),
    path('borrar_pelicula/<identificador>', views.borrar_pelicula, name="borrar_pelicula"),
    path('borrar_libro/<identificador>', views.borrar_libro, name="borrar_libro"),
    path('buscar_pelicula/', views.buscar_pelicula, name="buscar_pelicula"),
    path('buscar_serie/', views.buscar_serie, name="buscar_serie"),
    path('buscar_libro/', views.buscar_libro, name="buscar_libro"),


]