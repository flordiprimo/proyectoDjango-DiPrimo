from django import forms


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