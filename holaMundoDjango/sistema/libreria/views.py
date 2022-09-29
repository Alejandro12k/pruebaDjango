from html.entities import html5
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro #importando el modelo "libro", de ahí traeré la información
# Create your views here.
from .forms import LibroForm


def inicio(request):
    return render(request,'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    #print(libros)
    return render(request, 'libros/index.html',{'libros':libros})

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    #print(formulario)
    return render(request, 'libros/crear.html', {'formulario':formulario})

def editar(request):
    return render(request, 'libros/editar.html')