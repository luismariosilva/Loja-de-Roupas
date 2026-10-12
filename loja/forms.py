from django import forms
from loja.models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'categoria', 'preco', 'em_stock']