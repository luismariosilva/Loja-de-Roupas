from django.shortcuts import render, redirect
from loja.models import Produto




def produtos(request):
    produto = Produto.objects.all()
    context = {'produtos': produto}
    return render(request, 'loja/produtos.html', context)

