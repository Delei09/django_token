# Generated by Django 4.0.2 on 2022-02-09 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_livros_id_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='id_usuario_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livros_emprestado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='livros',
            name='livro_emprestado',
            field=models.BooleanField(default=False),
        ),
    ]
