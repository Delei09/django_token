# Generated by Django 4.0.2 on 2022-02-09 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_user_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('editora', models.CharField(max_length=255)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
                'ordering': ['autor'],
            },
        ),
    ]