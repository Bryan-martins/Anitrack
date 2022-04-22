# Generated by Django 3.2.9 on 2022-04-19 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banco', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.CharField(max_length=100, verbose_name='Data de início')),
                ('data_fim', models.CharField(max_length=100, verbose_name='Data de fim')),
                ('progress', models.CharField(max_length=100, verbose_name='Progresso(episódios)')),
                ('status', models.CharField(choices=[('assistindo', 'Assistindo'), ('pa', 'Pretendo Assistir'), ('completo', 'Completo'), ('reassistindo', 'Reassistindo'), ('pausado', 'Pausado'), ('dropei:)', 'Dropei:)')], default='PA', max_length=15)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco.bank')),
            ],
        ),
    ]