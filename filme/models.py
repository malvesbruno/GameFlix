from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

#criar os filmes

LISTA_CATEGORIAS = (
    ("BOM TRAMA", "trama"),
    ("AÇÃO", "ação"),
    ("OUTROS", "outros"),
    ("TERROR", 'terror'),
    ("FPS", "FPS"),
)


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

#criar episodios


class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name='episodios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_episodios', default='SOME STRING')
    video = models.URLField()

    def __str__(self):
        return self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")




