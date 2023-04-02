from django.shortcuts import render
from AppShortStories.models import Genero , Author, ShortStories
from AppShortStories.forms import BuscarGeneroform ,BuscarAuthorform ,BuscarStoriesform
from django.views.generic import ListView ,CreateView
from django.urls import reverse_lazy

def Inicio(request):
    return render(request,"AppShortStories/index.html")

##import pdb; pdb.set_trace() 
    ## linea par debug l para ver donde se quedo , n para sergir la linea , c para continuar

class BuscarGenero(ListView):
    model = Genero
    context_object_name = "generos"

    def get_queryset(self):
        f = BuscarGeneroform(self.request.GET)
        if f.is_valid():
           return Genero.objects.filter(descripcion__icontains =f.data["criterio_descripcion"]).all()
        return Genero.objects.all()

class GeneroCreate(CreateView):
    model = Genero
    success_url = reverse_lazy("genero-list")
    fields = '__all__'


class BuscarAuthor(ListView):
    model = Author
    context_object_name = "autores"

    def get_queryset(self):
        f = BuscarAuthorform(self.request.GET)
        if f.is_valid():
           return Author.objects.filter(apellido__icontains =f.data["criterio_apellido"]).all()
        return Author.objects.all()

class AuthorCreate(CreateView):
    model = Author
    success_url = reverse_lazy("autor-list")
    fields = '__all__'

class BuscarShortStories(ListView):
    model = ShortStories
    context_object_name = "cuentos"

    def get_queryset(self):
        f = BuscarStoriesform(self.request.GET)
        if f.is_valid():
           return ShortStories.objects.filter(titulo__icontains =f.data["criterio_titulo"]).all()
        return ShortStories.objects.all()

class ShortStoriesCreate(CreateView):
    model = ShortStories
    success_url = reverse_lazy("cuento-list")
    fields = '__all__'