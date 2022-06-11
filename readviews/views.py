from multiprocessing import context
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from readviews.models import datos_generales, serie, pelicula, libro
from readviews.forms import datos_generalesForm, seriesForm, peliculasForm, librosForm, BuscarPeliculaForm, BuscarSerieForm, BuscarLibroForm
from django.db.models import Q

def index(request):
    template = loader.get_template('readviews/index.html')
    series = serie.objects.all()
    peliculas = pelicula.objects.all()
    libros = libro.objects.all()
    context = {
    'series':series , 'peliculas':peliculas , 'libros':libros,
     'indice_serie' : True , 'indice_pelicula' : True,  'indice_libro' : True
    }
    return HttpResponse(template.render(context, request))

def index_series(request):
    series = serie.objects.all()
    template = loader.get_template('readviews/index.html')
    context = {
        'series': series, 'indice_serie' : True
    }
    return HttpResponse(template.render(context, request))

def index_peliculas(request):
    peliculas = pelicula.objects.all()
    template = loader.get_template('readviews/index.html')
    context = {
        'peliculas': peliculas,'indice_pelicula' : True
    }
    return HttpResponse(template.render(context, request))

def index_libros(request):
    libros = libro.objects.all()
    template = loader.get_template('readviews/index.html')
    context = {
        'libros': libros,'indice_libro' : True
    }
    return HttpResponse(template.render(context, request))



def agregar_serie(request):
    
    if request.method == "POST":
        form = seriesForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            comentarios = form.cleaned_data['comentarios']
            temporadas = form.cleaned_data['temporadas']
            plataforma = form.cleaned_data['plataforma']
            fecha_final = form.cleaned_data['fecha_final']
            serie(titulo=titulo, autor=autor, fecha_inicio=fecha_inicio, comentarios=comentarios,temporadas=temporadas, plataforma = plataforma, fecha_final=fecha_final).save()

            return HttpResponseRedirect("/readviews/")
    elif request.method == "GET":
        form = seriesForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'readviews/form_carga.html', {'form': form , 'indice_serie' : True})


def agregar_pelicula(request):
    
    if request.method == "POST":
        form = peliculasForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            comentarios = form.cleaned_data['comentarios']
            genero = form.cleaned_data['genero']
            plataforma = form.cleaned_data['plataforma']
            pelicula(titulo=titulo, autor=autor, fecha_inicio=fecha_inicio, comentarios=comentarios, plataforma = plataforma, genero = genero ).save()

            return HttpResponseRedirect("/readviews/")
    elif request.method == "GET":
        form = peliculasForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'readviews/form_carga.html', {'form': form , 'indice_pelicula': True})


def agregar_libro(request):
    
    if request.method == "POST":
        form = librosForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            autor = form.cleaned_data['autor']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            comentarios = form.cleaned_data['comentarios']
            fecha_final = form.cleaned_data['fecha_final']
            genero = form.cleaned_data['genero']
            libro(titulo=titulo, autor=autor, fecha_inicio=fecha_inicio, comentarios=comentarios, fecha_final=fecha_final, genero = genero ).save()

            return HttpResponseRedirect("/readviews/")
    elif request.method == "GET":
        form = librosForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'readviews/form_carga.html', {'form': form, 'indice_libro': True})


def borrar_serie(request, identificador):
    
    if request.method == "GET":
        series = serie.objects.filter(id=int(identificador)).first()
        if series:
            series.delete()
        return HttpResponseRedirect("/readviews/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def borrar_pelicula(request, identificador):
    
    if request.method == "GET":
        peliculas = pelicula.objects.filter(id=int(identificador)).first()
        if peliculas:
            peliculas.delete()
        return HttpResponseRedirect("/readviews/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def borrar_libro(request, identificador):
    
    if request.method == "GET":
        libros = libro.objects.filter(id=int(identificador)).first()
        if libros:
            libros.delete()
        return HttpResponseRedirect("/readviews/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def buscar_pelicula(request):
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarPeliculaForm(request.GET)
        if form_busqueda.is_valid():
            peliculas = pelicula.objects.filter(titulo__icontains = request.GET.get("palabra_a_buscar"))
            return render(request,"readviews/index.html", {'peliculas':peliculas, 'indice_pelicula':True})       
    elif request.method == "GET":
        form_busqueda = BuscarPeliculaForm()
        return render(request, "readviews/form_busqueda.html", {'form_busqueda':form_busqueda, 'indice_pelicula': True})

    else: return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

def buscar_serie(request):
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarSerieForm(request.GET)
        if form_busqueda.is_valid():
            series = serie.objects.filter(titulo__icontains = request.GET.get("palabra_a_buscar"))
            return render(request,"readviews/index.html", {'series':series, 'indice_serie':True})       
    elif request.method == "GET":
        form_busqueda = BuscarSerieForm()
        return render(request, "readviews/form_busqueda.html", {'form_busqueda':form_busqueda, 'indice_serie': True })

    else: return HttpResponseBadRequest("Error no conozco ese metodo para esta request")

def buscar_libro(request):
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarLibroForm(request.GET)
        if form_busqueda.is_valid():
            libros = libro.objects.filter(titulo__icontains = request.GET.get("palabra_a_buscar"))
            return render(request,"readviews/index.html", {'libros':libros, 'indice_libro':True})       
    elif request.method == "GET":
        form_busqueda = BuscarLibroForm()
        return render(request, "readviews/form_busqueda.html", {'form_busqueda':form_busqueda, 'indice_libro': True })

    else: return HttpResponseBadRequest("Error no conozco ese metodo para esta request")