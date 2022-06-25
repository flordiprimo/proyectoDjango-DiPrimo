from django.shortcuts import redirect, render

from .forms import CamisaFormulario, PantalonFormulario, RemeraFormulario
from .models import *


def index(request):
    return render(request, 'tienda/index.html')

def remeras(request):
    remeras = Remera.objects.all()
    context = {'remeras': remeras}
    return render(request, "tienda/remeras.html", context )

def pantalones(request):
    pantalones = Pantalon.objects.all()
    context = {'pantalones': pantalones}
    return render(request, "tienda/pantalones.html", context )

def camisas(request):
    camisas = Camisa.objects.all()
    context = {'camisas': camisas}
    return render(request, "tienda/camisas.html", context )

def crearRemera(request):
    
    if request.method == 'POST':
        formulario = RemeraFormulario(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            remera = Remera(marca=informacion['marca'],talle=informacion['talle'],color=informacion['color'],precio=informacion['precio'],)
            remera.save()
            return redirect('remeras')
        else:
            return render(request, "tienda/remeraFormulario.html", {"form": formularioVacio} )
    else:
       formularioVacio = RemeraFormulario()

    return render(request, "tienda/remeraFormulario.html", {"form": formularioVacio} )

def crearCamisa(request):
    
    if request.method == 'POST':
        formulario = CamisaFormulario(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            camisa = Camisa(marca=informacion['marca'],talle=informacion['talle'],color=informacion['color'],precio=informacion['precio'],)
            camisa.save()
            return redirect('camisas')
        else:
            return render(request, "tienda/camisaFormulario.html", {"form": formularioVacio} )
    else:
       formularioVacio = CamisaFormulario()

    return render(request, "tienda/camisaFormulario.html", {"form": formularioVacio} )

def crearPantalon(request):
    
    if request.method == 'POST':
        formulario = PantalonFormulario(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            pantalon = Pantalon(marca=informacion['marca'],talle=informacion['talle'],color=informacion['color'],precio=informacion['precio'],)
            pantalon.save()
            return redirect('pantalones')
        else:
            return render(request, "tienda/pantalonFormulario.html", {"form": formularioVacio} )
    else:
       formularioVacio = PantalonFormulario()

    return render(request, "tienda/pantalonFormulario.html", {"form": formularioVacio} )

def buscarRemera(request):
    
    if request.method == 'POST':
        marca = request.POST['marca']
        marcas = Remera.objects.filter(marca__icontains=marca)
        return render(request,'tienda/busqueda-remera.html', {'marcas': marcas} )
    
    else:
        marcas = []
        return render(request,'tienda/busqueda-remera.html', {'marcas': marcas} )

def buscarPantalon(request):
    
    if request.method == 'POST':
        marca = request.POST['marca']
        marcas = Pantalon.objects.filter(marca__icontains=marca)
        return render(request,'tienda/busqueda-pantalon.html', {'marcas': marcas} )
    
    else:
        marcas = []
        return render(request,'tienda/busqueda-pantalon.html', {'marcas': marcas} )

def buscarCamisa(request):
    
    if request.method == 'POST':
        marca = request.POST['marca']
        marcas = Camisa.objects.filter(marca__icontains=marca)
        return render(request,'tienda/busqueda-camisa.html', {'marcas': marcas} )
    
    else:
        marcas = []
        return render(request,'tienda/busqueda-camisa.html', {'marcas': marcas} )
