# Generated by Django 4.1.7 on 2023-04-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFutbol', '0003_alter_jugadores_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='equipos'),
        ),
    ]
