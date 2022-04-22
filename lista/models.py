from django.db import models
from django.contrib.auth import get_user_model
from banco.models import Bank


class ListaUser(models.Model):
    STATUS = (
        ('assistindo', 'Assistindo'),
        ('pa', 'Pretendo Assistir'),
        ('completo', 'Completo'),
        ('reassistindo', 'Reassistindo'),
        ('pausado', 'Pausado'),
        ('dropei', 'Dropei :)')
    )

    data_inicio = models.CharField(max_length=100, verbose_name='Data de início')
    data_fim = models.CharField(max_length=100, verbose_name='Data de fim')
    progress = models.CharField(max_length=100, verbose_name='Progresso(episódios)')
    status = models.CharField(max_length=15, choices=STATUS, default='pa')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    anime = models.ForeignKey(Bank ,on_delete=models.CASCADE)
