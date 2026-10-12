from django.shortcuts import render, redirect
from loja.models import Produto
from loja.forms import ProdutoForm




def produtos(request):
    produto = Produto.objects.all()
    context = {'produtos': produto}
    return render(request, 'loja/produtos.html', context)


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()
    return render(request, 'loja/adicionar_produto.html', {'form': form})


def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'loja/adicionar_produto.html', {'form': form})


def apagar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos')
    return render(request, 'loja/apagar_produto.html', {'produto': produto})


