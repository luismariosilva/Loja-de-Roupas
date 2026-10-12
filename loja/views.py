from django.shortcuts import render
from django.http import HttpResponse
from loja.models import Produto, Marca, Categoria



def produtos(request):
    produto = Produto.objects.all()
    context = ('produtos', produto)
    return render(request, 'loja/produtos.html', context)

def marcas(request):
    marca = Marca.objects.all()
    context = ('marcas', marca)
    return render(request, 'loja/marcas.html', context)

def categorias(request):
    categoria = Categoria.objects.all()
    context = ('categorias', categoria)
    return render(request, 'loja/categorias.html', context)
