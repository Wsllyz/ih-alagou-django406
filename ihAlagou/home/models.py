from django.db import models

# Create your models here.

class leitura(models.Model):
    distancia = models.IntegerField()
    temperatura = models.IntegerField()
    statusBateria = models.IntegerField()
    timestamp = models.TextField()