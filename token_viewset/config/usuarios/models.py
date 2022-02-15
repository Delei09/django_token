from enum import unique
from pyexpat import model
from tabnanny import verbose
import uuid
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.db import models
from django.utils.translation import gettext as _



class User(AbstractBaseUser, PermissionsMixin):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100 ,verbose_name=_('Nome'))
    email = models.EmailField(max_length=100, unique=True, verbose_name=_('Email'))
    telefone = models.CharField(max_length=15, blank=True, verbose_name=_('Telefone'))
    password = models.CharField(max_length=255, verbose_name=_('Senha'))
    # photo = models.CharField(max_length=100, blank=True, verbose_name=_('Foto perfil'))
    # cep = models.CharField(max_length=9, blank=True, verbose_name=_('CEP'))
    # rua = models.CharField(max_length=100, blank=True, verbose_name=_('Endereço'))
    # numero = models.CharField(max_length=100, blank=True, verbose_name=_('Nº'))
    # bairro = models.CharField(max_length=100, blank=True, verbose_name=_('Bairro'))
    # cidade = models.CharField(max_length=100, blank=True, verbose_name=_('Cidade'))
    # uf = models.CharField(max_length=2, blank=True, verbose_name=_('UF'))
    is_active = models.BooleanField(default=True, verbose_name='Ativo?')
    is_staff = models.BooleanField(default=False, verbose_name='É da equipe de administração?')
    admin = models.BooleanField(default=False, verbose_name='É superUsuario?')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Data da Inclusão'))
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de Criação'))
    updatedAt = models.DateTimeField(auto_now=True, verbose_name=_('Data de Modificação'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    USERNAME_FIELDS = ['nome', 'email']

    def __str__(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
class Livros(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True , related_name='livros' )
    livro_emprestado = models.BooleanField(default=False)
    id_usuario_emprestado =  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True , related_name='livros_emprestado' )
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['autor']
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
 
