# Generated by Django 5.0.7 on 2024-08-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(upload_to='static/polls/imagens'),
        ),
    ]