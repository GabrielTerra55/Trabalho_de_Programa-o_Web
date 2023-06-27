from django.contrib.postgres.fields import ArrayField
from django.db import models

class Pessoa(models.Model):
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	amigos = ArrayField(models.IntegeerField())
	def __str__(self):
		return self.nome