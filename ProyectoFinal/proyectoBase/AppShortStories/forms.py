from django import forms

class GeneroForm(forms.Form):
    descripcion = forms.CharField(max_length=50)
    estado = forms.BooleanField(required = False,label='Activo')

class BuscarGeneroform(forms.Form):
    criterio_descripcion = forms.CharField(max_length=50)

class BuscarAuthorform(forms.Form):
    criterio_apellido = forms.CharField(max_length=50)

class BuscarStoriesform(forms.Form):
    criterio_titulo = forms.CharField(max_length=50)