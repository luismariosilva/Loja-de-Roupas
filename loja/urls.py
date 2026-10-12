from django.urls import path
from loja import views


urlpatterns = [
    path('produtos', views.produtos, name='produtos'),
    path('marcas', views.marcas, name='marcas'),
    path('categorias', views.categorias, name='categorias'),
]
