# Generated by Django 5.1 on 2024-10-21 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='subtitulo',
        ),
    ]
