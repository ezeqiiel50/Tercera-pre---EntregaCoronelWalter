from django.urls import path
from AppShortStories.views import (Inicio,BuscarGenero,BuscarAuthor,BuscarShortStories,GeneroCreate,AuthorCreate,
                                    ShortStoriesCreate)

urlpatterns =[
    path('',Inicio, name="inicio"),
    path('genero/list', BuscarGenero.as_view(), name="genero-list"),
    path('genero/create', GeneroCreate.as_view(), name="genero-create"),
    path('author/list', BuscarAuthor.as_view(), name="autor-list"),
    path('author/create', AuthorCreate.as_view(), name="autor-create"),
    path('stories/list', BuscarShortStories.as_view(), name="cuento-list"),
    path('stories/create', ShortStoriesCreate.as_view(), name="cuento-create"),
]