# Generated by Django 5.0.7 on 2024-08-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(upload_to='polls/imagens'),
        ),
    ]
