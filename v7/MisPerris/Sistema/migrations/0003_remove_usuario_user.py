# Generated by Django 2.1.2 on 2018-11-04 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0002_usuario_fechanacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
    ]
