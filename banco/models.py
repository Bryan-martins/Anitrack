from django.db import models


class Bank(models.Model):
    titulo_original = models.CharField(max_length=100, verbose_name='Título Original', unique=True)
    titulo_ingles = models.CharField(max_length=100, verbose_name='Título em inglês', unique=True)
    duracao_do_episodio = models.CharField(max_length=100, verbose_name='Duração do episódio')
    inicio = models.CharField(max_length=100, verbose_name='Data de início')
    status_obra = models.CharField(max_length=100, verbose_name='Status')
    temporada = models.CharField(max_length=100, verbose_name='Temporada de lançamento')
    estudio = models.CharField(max_length=100, verbose_name='Estudio')
    origem = models.CharField(max_length=100, verbose_name='Pais de origem')
    generos = models.CharField(max_length=100, verbose_name='Gêneros')
    imagens = models.ImageField(upload_to='media')
    banner = models.ImageField(upload_to='media')
    descricao = models.CharField(max_length=1000, verbose_name='Descrição')
    #media_da_comunidade = 

    def __str__(self):
        return '{}'.format(self.titulo_ingles)
