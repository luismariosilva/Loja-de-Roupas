from django.db import models


class Categoria(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome


class Marca(models.Model):
	nome = models.CharField(max_length=80)
	pais_origem = models.CharField(max_length=50)

	def __str__(self):
		return self.nome


class Produto(models.Model):
	nome = models.CharField(max_length=150)
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	categoria = models.ManyToManyField(Categoria)
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	em_stock = models.BooleanField(default=True)

	def __str__(self):
		return self.nome
