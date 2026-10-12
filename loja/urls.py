from django.urls import path
from loja import views


urlpatterns = [
    path('produto/', views.produtos, name='produtos'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('apagar/<int:produto_id>/', views.apagar_produto, name='apagar_produto'),
]
