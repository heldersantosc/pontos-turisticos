# Generated by Django 4.1.1 on 2022-09-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_rename_atracaomodel_atracao'),
        ('core', '0003_rename_pontoturisticomodel_pontoturistico'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.atracao'),
        ),
    ]
