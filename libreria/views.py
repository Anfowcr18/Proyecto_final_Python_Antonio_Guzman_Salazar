from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import libro
from.forms import LibroForm
from.models import usuario
from.forms import UsuarioForm
from.models import adquisicion
from.forms import AdquisicionForm

def inicio (request):
    return render(request,'paginas/inicio.html')
def nosotros (request):
    return render(request,'paginas/nosotros.html')

def libros (request):
    libros=libro.objects.all()
    print(libros)
    return render(request,'libros/index.html',{'libros':libros})
def crear (request):
    formulario=LibroForm(request.Post or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request,'libros/crear.html',{'formulario':formulario})   
def editar (request,id):
    libro=libro.objects.get(id=id)
    formulario=LibroForm(request.Post or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})
def eliminar(request,id):
    libro=libro.objects.get(id=id)
    libro.delete()
    return render('libros')

    
def usuarios (request):
    usuarios=usuario.objects.all()
    print(usuarios)
    return render(request,'usuario/indexus.html',{'usuarios':usuarios})
def crearus (request):
    formulario=UsuarioForm(request.Post or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request,'usuarios/crearus.html',{'formulario':formulario})   
def editarus (request,id):
    editar=editar.objects.get(id=id)
    formulario=UsuarioForm(request.Post or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    return render(request,'usuarios/editarus.html',{'formulario':formulario})
def eliminarus(request,id):
    usuarios=usuario.objects.get(id=id)
    usuarios.delete()
    return render('usuarios')

def adquisiciones (request):
    adquisiciones=adquisicion.objects.all()
    print(adquisiciones)
    return render(request,'usuario/indexus.html',{'adquisiciones':adquisiciones})
def creara (request):
    formulario=AdquisicionForm(request.Post or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Adquisiciones')
    return render(request,'usuarios/crearus.html',{'formulario':formulario})   
def editara (request,id):
    editar=editar.objects.get(id=id)
    formulario=AdquisicionForm(request.Post or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('Adquisiciones')
    return render(request,'usuarios/editara.html',{'formulario':formulario})
def eliminara(request,id):
    Adquisiciones=adquisicion.objects.get(id=id)
    Adquisiciones.delete()
    return render('adquisiciones')
# Create your views here.
