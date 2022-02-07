# Generated by Django 4.0.2 on 2022-02-07 19:16

import django.contrib.auth.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=15, unique=True, verbose_name='CPF')),
                ('password', models.CharField(max_length=32, verbose_name='Senha')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('telefone', models.CharField(blank=True, max_length=15, verbose_name='Telefone')),
                ('cep', models.CharField(blank=True, max_length=9, verbose_name='CEP')),
                ('rua', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(blank=True, max_length=100, verbose_name='Nº')),
                ('bairro', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(blank=True, max_length=2, verbose_name='UF')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('is_staff', models.BooleanField(default=False, verbose_name='É da equipe de administração?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data da Inclusão')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Data de Modificação')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
