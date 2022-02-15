from dataclasses import fields
from urllib import request
from xml.parsers.expat import model
from rest_framework import serializers
from usuarios.models import User , Livros

class UsuariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id" , 'nome' , 'email' , 'telefone', 'password']
        
class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'
        
class UsuarioLivrosSerializer(serializers.ModelSerializer):
    # livros = LivrosSerializer(many = True, read_only=True )
    # Se nao estiver o related_name no model o django joga algo automatico e deve usar _set ex: livros_set

    livros = serializers.HyperlinkedRelatedField(many=True, view_name='livros-detail', read_only=True)
    class Meta:
        model = User
        fields = ['id' , 'nome' , 'email', 'livros' ]        
        
class LivrosEmprestadosUsuarioSerializer(serializers.ModelSerializer):
    # livros = LivrosSerializer(many = True, read_only=True )
    # Se nao estiver o related_name no model o django joga algo automatico e deve usar _set ex: livros_set

    livros = serializers.HyperlinkedRelatedField(many=True, view_name='livros-detail', read_only=True)
    livros_emprestado = serializers.HyperlinkedRelatedField(many=True, view_name='livros-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id' , 'nome' , 'email', 'livros', 'livros_emprestado' ]  