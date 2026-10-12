from django.urls import path
from loja import views


urlpatterns = [
    path('produto/', views.produtos, name='produtos'),
]
