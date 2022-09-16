# Generated by Django 4.1.1 on 2022-09-16 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0007_pontoturistico_enderecos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pontoturistico',
            name='enderecos',
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='enderecos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]
