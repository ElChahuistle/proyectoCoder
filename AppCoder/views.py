from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso


# Create your views here.
def curso(request):
    curso = Curso(nombre='Backend', camada='12345')
    curso.save()
    respuesta = f'Curso: {curso.nombre}, Camada: {curso.camada}'

    return HttpResponse(respuesta)


def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

