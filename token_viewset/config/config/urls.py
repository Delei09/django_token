"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers
from usuarios.views import UsuariosViewset , CadastroUsuarioApiview , ResetSenhaApiview, LivrosViewset, UsuarioLivrosApiview, LivrosEmprestadosUsuarioApiview, EmprestarLivroApiview, DevolverLivroApiview

rotas = routers.DefaultRouter()
rotas.register('usuarios', UsuariosViewset, basename='usuarios')
rotas.register('livros', LivrosViewset, basename='livros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(rotas.urls)),
    path('cadastro/', CadastroUsuarioApiview.as_view(), name='cadastro'),
    path('novasenha/' , ResetSenhaApiview.as_view(), name='nova_senha' ),
    path('usuario/livros/', UsuarioLivrosApiview.as_view(), name='usuario_livros'),
    path('usuario/livros-emprestados/', LivrosEmprestadosUsuarioApiview.as_view(), name='usuario_livros_emprestado'),
    path('emprestar/' , EmprestarLivroApiview.as_view(), name='emprestar_livro' ),
    path('devolver/' , DevolverLivroApiview.as_view(), name='devolver_livro' ),

]
