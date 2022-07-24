from django.shortcuts import redirect, render

from .forms import AvatarForm, UserEditForm, UserRegisterForm
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User

#creo un mixin para Staff Required CBVs
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

def entrada(request):
    return redirect("inicio")

def index(request):
    
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url = "/media/avatares/generico.png"
        return render(request, 'tienda/index.html', {'url':url})
    
    else:
        return render(request, 'tienda/index.html')

def not_found (request,exception):
    return render(request, 'tienda/404.html')


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect('login')
        else:
            return redirect('login')
            
    form = AuthenticationForm()
    
    return render(request, 'tienda/login.html', {'form': form})

def register_request(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('mi_perfil')
            else:
                return redirect('login')
        
        return render(request, 'tienda/register.html', {'form': form})
            
    form = UserRegisterForm()
    
    return render(request, 'tienda/register.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect('inicio')

@login_required
def editar_perfil(request):
    user = request.user
    
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            info = form.cleaned_data
            user.email = info['email']
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            user.save()
            
            return redirect('mi_perfil')
    else:
        form = UserEditForm(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render(request, 'tienda/editar_perfil.html', {'form': form})

@login_required
def agregar_avatar(request):
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatar(usuario=user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            
            return redirect('mi_perfil')
    else:
        form = AvatarForm()
    
    return render(request, 'tienda/agregar_avatar.html', {'form': form})

@login_required
def mi_perfil(request):
    user = request.user
    
    return render(request, 'tienda/mi_perfil.html', {'user': user})
    

class PasswordResetByUser(LoginRequiredMixin,PasswordChangeView):
    template_name = 'tienda/cambiar_password.html'
    success_url = '/tienda/mi-perfil'
 
def about(request):
    
    return render(request, 'tienda/about.html',)
        
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

def buscarRemera(request):
    
    if request.method == 'POST':
        modelo = request.POST['modelo']
        modelos = Remera.objects.filter(modelo__icontains=modelo)
        return render(request,'tienda/busqueda-remera.html', {'modelos': modelos} )
    
    else:
        modelos = []
        return render(request,'tienda/busqueda-remera.html', {'modelos': modelos} )

def buscarPantalon(request):
    
    if request.method == 'POST':
        modelo = request.POST['modelo']
        modelos = Pantalon.objects.filter(modelo__icontains=modelo)
        return render(request,'tienda/busqueda-pantalon.html', {'modelos': modelos} )
    
    else:
        modelos = []
        return render(request,'tienda/busqueda-pantalon.html', {'modelos': modelos} )

def buscarCamisa(request):
    
    if request.method == 'POST':
        modelo = request.POST['modelo']
        modelos = Camisa.objects.filter(modelo__icontains=modelo)
        return render(request,'tienda/busqueda-camisa.html', {'modelos': modelos} )
    
    else:
        modelos = []
        return render(request,'tienda/busqueda-camisa.html', {'modelos': modelos} )

@staff_member_required
def editarProductos(request):
        return render(request,'tienda/editar_productos.html', {} )



class RemerasList(StaffRequiredMixin,ListView): 
    model = Remera
    template_name = "tienda/remeras_list.html" 
    
class RemeraDetail(DetailView): 
        model = Remera
        template_name = "tienda/remera_detail.html"


class RemeraCreate(StaffRequiredMixin,CreateView): 
        model = Remera
        success_url = "/tienda/remera/list"
        fields = ['modelo', 'talle', 'color', 'precio', 'descripcion', 'imagen']

   
class RemeraUpdate(StaffRequiredMixin,UpdateView): 
        model = Remera
        success_url = "/tienda/remera/list"
        fields = ['modelo', 'talle', 'color', 'precio', 'descripcion', 'imagen']
    

class RemeraDelete(StaffRequiredMixin,DeleteView): 
        model = Remera
        success_url = "/tienda/remera/list"


class CamisasList(StaffRequiredMixin,ListView): 
    model = Camisa
    template_name = "tienda/camisas_list.html" 
    
class CamisaDetail(DetailView): 
        model = Camisa
        template_name = "tienda/camisa_detail.html"

       
class CamisaCreate(StaffRequiredMixin,CreateView): 
        model = Camisa
        success_url = "/tienda/camisa/list"
        fields = ['modelo', 'talle', 'color', 'precio', 'descripcion', 'imagen']

class CamisaUpdate(StaffRequiredMixin,UpdateView): 
        model = Camisa
        success_url = "/tienda/camisa/list"
        fields = ['modelo', 'talle', 'color', 'precio', 'descripcion', 'imagen']
    
class CamisaDelete(StaffRequiredMixin,DeleteView): 
        model = Camisa
        success_url = "/tienda/camisa/list"           

class PantalonesList(StaffRequiredMixin,ListView): 
    model = Pantalon
    template_name = "tienda/pantalones_list.html" 

class PantalonDetail(DetailView): 
        model = Pantalon
        template_name = "tienda/pantalon_detail.html"

class PantalonCreate(StaffRequiredMixin,CreateView): 
        model = Pantalon
        success_url = "/tienda/pantalon/list"
        fields = ['modelo', 'talle', 'color', 'precio', 'descripcion', 'imagen']

class PantalonUpdate(StaffRequiredMixin,UpdateView): 
        model = Pantalon
        success_url = "/tienda/pantalon/list"
        fields = ['modelo', 'talle', 'color', 'precio', 'descripcion', 'imagen']

class PantalonDelete(StaffRequiredMixin,DeleteView): 
        model = Pantalon
        success_url = "/tienda/pantalon/list"           