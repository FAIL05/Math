# Generated by Django 5.0.7 on 2025-01-10 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_usuario_foto_perfil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Material_de_Estudo',
        ),
        migrations.DeleteModel(
            name='Opções_de_Resposta',
        ),
        migrations.RemoveField(
            model_name='respostas',
            name='id_questões',
        ),
        migrations.RemoveField(
            model_name='respostas',
            name='id_usuarios',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Respostas',
        ),
    ]
