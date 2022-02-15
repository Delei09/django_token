from django.forms import ValidationError
from rest_framework import viewsets ,permissions, filters, generics
from rest_framework.views import Response , APIView 
from usuarios.models import User, Livros
from usuarios.serializer import UsuariosSerializer, LivrosSerializer, UsuarioLivrosSerializer, LivrosEmprestadosUsuarioSerializer
from usuarios.validators import *
from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend 
from django.contrib.auth.hashers import check_password
import jwt

class UsuariosViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', "email"]
    # filterset_fields = ['ativo']

class CadastroUsuarioApiview(APIView):
      
    def post(self, request):
        try:
            password = request.data['password']
            nome = request.data['nome']
            email = request.data['email']
            telefone = request.data['telefone']
            if(nome == ''):
                raise serializers.ValidationError({"nome" : "Campo invalido"}) 
            if(email == ''):
                raise serializers.ValidationError({"email" : "Campo invalido"}) 
            if(telefone == ''):
                raise serializers.ValidationError({"telefone" : "Campo invalido"}) 
            if(password == ''):
                raise serializers.ValidationError({"senha" : "Campo invalido"}) 
            if not nome_valido(nome) :
                raise serializers.ValidationError({"nome" : "O nome nao pode conter numeros"}) 
            if  email_valido(email):
                raise serializers.ValidationError({'email':"Email já existe" })
            if not celular_valido(telefone):
                raise serializers.ValidationError({'celular':" Exemplos válidos: 35997111055/ 0335997221055 /  34715265 /  03562655656"})
            if not senha_valido(password):
                raise serializers.ValidationError({"Senha":"A senha deve conter no minimo 8 caracteres, 1 letra maiscula, 1 numero, 1 caractere especial"})
            
            user = User(
                nome = nome ,
                email = email,
                telefone = telefone,
            )
            admin = request.data['admin']
            if(admin):
                user.is_superuser = True
            user.set_password(password)
            user.save()
            return Response('Usuario Criado Com Sucesso!!!')
        except KeyError as e:
            raise serializers.ValidationError(f'campo {e} esta faltando')
        except ValidationError  :
            return ValidationError

class ResetSenhaApiview(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            senha = request.data['senha']
            confirmacao_senha = request.data['confirmacao_senha']
            authorization = request.headers['Authorization']
            token = authorization[7: ]
            
            if not senha_valido(senha):
                raise serializers.ValidationError({"Senha":"A senha deve conter no minimo 8 caracteres, 1 letra maiscula, 1 numero, 1 caractere especial"})
            
            if(senha == confirmacao_senha):
                usuario = jwt.decode(token, key='django-insecure--4b654bps&$mf)5*c_*lsf!%(dt9iwbo&uftb%)lcc0+u0gdw0', algorithms=['HS256'])
                id = usuario['user_id']
                usuario = User.objects.get(pk = id)
                serializer = UsuariosSerializer(usuario)
                senha_banco_criptografada = serializer.data['password']
                corresponde = check_password(password=senha, encoded=senha_banco_criptografada)
                if(corresponde):
                    raise serializers.ValidationError({"Senha":"Não pode ser a mesma senha, insira outra senha"})
                usuario.set_password(senha)
                usuario.save()
                return Response("Senha alterada com sucesso!")
            return Response("Senha não são iguais")
        except KeyError as e :
            return Response(f'Campo {e} ausente')
        
class LivrosViewset(viewsets.ModelViewSet):
        
        queryset = Livros.objects.all()
        serializer_class = LivrosSerializer
        permission_classes = [permissions.IsAuthenticated]
        
class UsuarioLivrosApiview(generics.ListAPIView):
    
    # def get(self, request):
    #         authorization = request.headers['Authorization']
    #         token = authorization[7: ]
    #         usuario = jwt.decode(token, key='django-insecure--4b654bps&$mf)5*c_*lsf!%(dt9iwbo&uftb%)lcc0+u0gdw0', algorithms=['HS256'])
    #         id = usuario['user_id']
    #         usuario = User.objects.filter(id=id)
    #         print(usuario)
    #         serializer = UsuarioLivrosSerializer(usuario)
    #         return Response(serializer.data)
    serializer_class = UsuarioLivrosSerializer
    def get_queryset(self):
        authorization = self.request.headers['Authorization']
        token = authorization[7: ]
        usuario = jwt.decode(token, key='django-insecure--4b654bps&$mf)5*c_*lsf!%(dt9iwbo&uftb%)lcc0+u0gdw0', algorithms=['HS256'])
        id = usuario['user_id']
        usuario = User.objects.filter(id=id)
        print(usuario)
        return usuario
    
class LivrosEmprestadosUsuarioApiview(generics.ListAPIView):
    serializer_class = LivrosEmprestadosUsuarioSerializer
    def get_queryset(self):
        authorization = self.request.headers['Authorization']
        token = authorization[7: ]
        usuario = jwt.decode(token, key='django-insecure--4b654bps&$mf)5*c_*lsf!%(dt9iwbo&uftb%)lcc0+u0gdw0', algorithms=['HS256'])
        id = usuario['user_id']
        usuario = User.objects.filter(id=id)
        return usuario
    
class EmprestarLivroApiview(APIView):
    
    def post(self, request):
        try:
            id_livro = request.data['id_livro']
            livro_get = Livros.objects.get(pk=id_livro)    
            serializer = LivrosSerializer(livro_get)
            emprestado = serializer.data['livro_emprestado']
            id_usuario = serializer.data['id_usuario']
            if(emprestado):
                id_usuario_emprestado = serializer.data['id_usuario_emprestado']
                return Response(f"Livro já esta emprestado para o usuario: {id_usuario_emprestado}")
            
            livro = Livros.objects.filter(pk=id_livro)
            authorization = self.request.headers['Authorization']
            token = authorization[7: ]
            usuario = jwt.decode(token, key='django-insecure--4b654bps&$mf)5*c_*lsf!%(dt9iwbo&uftb%)lcc0+u0gdw0', algorithms=['HS256'])
            id = usuario['user_id']
            print(str(id_usuario) == str(id) )
            print(id)
            print(id_usuario)
            if( str(id) == str(id_usuario) ):
                return Response(f'Voce não pode emprestar um livro pra voce mesmo')
            
            livro.update(livro_emprestado=True, id_usuario_emprestado=id)
            
            return Response("Livro emprestado com sucesso!")
        except KeyError as e :
            return Response(f'Campo {e} ausente')
        except ValidationError as e :
            return Response(f' {e} ')
        except:
             return Response(f'ERRO SERVIDOR')
        
class DevolverLivroApiview(APIView):
    def post(self, request):
        try:   
            id_livro = request.data['id_livro']
            try:
                livro_get = Livros.objects.get(pk=id_livro)    
            except:
                raise serializers.ValidationError("ID incorreto")    
            serializer = LivrosSerializer(livro_get)
            emprestado = serializer.data['livro_emprestado']
            id_usuario_emprestado = serializer.data['id_usuario_emprestado']
            if(not emprestado):
                return Response(f"Livro não esta emprestado para nenhum usuario")
            
            livro = Livros.objects.filter(pk=id_livro)
            authorization = self.request.headers['Authorization']
            token = authorization[7: ]
            usuario = jwt.decode(token, key='django-insecure--4b654bps&$mf)5*c_*lsf!%(dt9iwbo&uftb%)lcc0+u0gdw0', algorithms=['HS256'])
            id = usuario['user_id']
            print(str(id_usuario_emprestado) == str(id) )
            print(id)
            print(id_usuario_emprestado)
            if( str(id) == str(id_usuario_emprestado) ):
                livro.update(livro_emprestado=False, id_usuario_emprestado='')
                return Response("Livro devolvido com sucesso!")
            return Response("Usuario que emprestou é diferente do que esta devolvendo!")
        
        except KeyError as e :
            return Response(f'Campo {e} ausente')
        except ValidationError as e :
            print(e)
            return  e
        except :
            return "Deu RUIM"
        