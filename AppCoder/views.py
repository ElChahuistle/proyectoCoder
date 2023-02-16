from django.shortcuts import redirect, render
from django.http import HttpResponse

from AppCoder.forms import CursoFormulario, ProfesorFormulario

from AppCoder.models import Curso, Profesor


# Create your views here.
# def curso(request):
#     curso = Curso(nombre='Backend', camada='12345')
#     curso.save()
#     respuesta = f'Curso: {curso.nombre}, Camada: {curso.camada}'
#
#     return HttpResponse(respuesta)


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


def curso_formulario(request):
    # if request.method == 'POST':
    #     curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    #     curso.save()
    #     return redirect('inicio')

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return redirect('inicio')

    mi_formulario = CursoFormulario()

    return render(request, 'AppCoder/curso-formulario.html', {'formulario_curso:': mi_formulario})


def profesor_formulario(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                email=informacion['email'],
                                profesion=informacion['profesion'])
            profesor.save()
            return redirect('inicio')
    else:
        mi_formulario = ProfesorFormulario()
        return render(request, 'AppCoder/profesor-formulario.html', {'formulario_profesor:': mi_formulario})


def busqueda_camada(request):
    return render(request, 'AppCoder/busqueda-camada.html')


def buscar(request):
    if request.GET['camada']:
        mi_camada = request.GET['camada']
        resultado = Curso.objects.filter(camada__icontains=mi_camada)

        return render(request, 'AppCoder/resultados-busqueda.html', {'cursos': resultado, 'camada': mi_camada})

    respuesta = 'No se encontro esa camada'
    return HttpResponse(respuesta)


def formulario(request):
    return render(request, 'AppCoder/formulario.html')
