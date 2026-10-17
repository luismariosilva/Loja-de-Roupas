from django.shortcuts import render, redirect
from loja.models import Produto
from loja.forms import ProdutoForm
from django.contrib.auth.decorators import login_required


@login_required
def produtos(request):
    produto = Produto.objects.all()
    context = {'produtos': produto}
    return render(request, 'loja/produtos.html', context)


@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()
    return render(request, 'loja/adicionar_produto.html', {'form': form, 'editando': False})

@login_required
def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'loja/adicionar_produto.html', {'form': form, 'editando': True})

@login_required
def apagar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos')
    return render(request, 'loja/apagar_produto.html', {'produto': produto})


