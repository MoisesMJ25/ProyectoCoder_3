# Generated by Django 4.1.7 on 2023-04-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFutbol', '0002_alter_equipo_categoria_alter_equipo_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugadores',
            name='nombre',
            field=models.CharField(max_length=10),
        ),
    ]
