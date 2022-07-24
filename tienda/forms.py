from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar


class RemeraFormulario(forms.Form):
    marca = forms.CharField(max_length=30, label='Marca')
    TALLES = (
    (1, 'XS'),
    (2, 'S'),
    (3, 'M'),
    (4, 'L'),
    (5, 'XL'),
    )
    talle = forms.ChoiceField(choices=TALLES, label='Talle')
    color = forms.CharField(max_length=15, label='Color')
    precio = forms.FloatField(label='Precio')
    imagen = forms.ImageField(label='Imagen')
    
class CamisaFormulario(forms.Form):
    marca = forms.CharField(max_length=30, label='Marca')
    TALLES = (
    (1, 'XS'),
    (2, 'S'),
    (3, 'M'),
    (4, 'L'),
    (5, 'XL'),
    )
    talle = forms.ChoiceField(choices=TALLES, label='Talle')
    color = forms.CharField(max_length=15, label='Color')
    precio = forms.FloatField(label='Precio: ')
    imagen = forms.ImageField(label='Imagen')

class PantalonFormulario(forms.Form):
    marca = forms.CharField(max_length=30, label='Marca')
    TALLES = (
    (1, 'XS'),
    (2, 'S'),
    (3, 'M'),
    (4, 'L'),
    (5, 'XL'),
    )
    talle = forms.ChoiceField(choices=TALLES, label='Talle')
    color = forms.CharField(max_length=15, label='Color')
    precio = forms.FloatField(label='Precio')
    imagen = forms.ImageField(label='Imagen')
    
class UserRegisterForm(UserCreationForm):
    email: forms.EmailField(label='Email')
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False,) 
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False,)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'password1', 'password2',]

        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen = forms.ImageField(label='Imagen de perfil')
    
    class Meta:
        model = Avatar
        fields = ['imagen'] 