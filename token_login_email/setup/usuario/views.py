from rest_framework.views import APIView , Response
from usuario.models import User

class CadastroApiview(APIView):
    def post(self, request):
        try :
            nome = request.data['nome']
            cpf = request.data['cpf']
            password = request.data['password']
            email = request.data['email']
            telefone = request.data['telefone']
            cep = request.data['cep']
            rua = request.data['rua']
            numero = request.data['numero']
            bairro = request.data['bairro']
            cidade = request.data['cidade']
            uf = request.data['uf']
            is_staff = request.data['admin']
            
            user = User(
                nome = nome ,
                cpf = cpf ,
                password = password ,
                email = email,
                telefone = telefone,
                cep = cep,
                rua = rua,
                numero = numero,
                bairro = bairro,
                cidade = cidade,
                uf =  uf,
                is_staff = is_staff
            )
            user.is_staff = True
            user.set_password(password)
            user.save()
            return Response(user.get_email_field_name())
        except:
            return Response("Campo invalido")
        
     
    
#     {
#             "nome" :"vanderlei de oliveira lemos",
#             "cpf":"11111111111",
#             "password":"12345678" ,
#             "email" :"vanderlei_09@outlook.com",
#             "telefone":" 35997111055",
#             "cep":"37540000",
#             "rua":"rua",
#             "numero":"numero",
#             "bairro":"bairro",
#             "cidade":"cidade",
#             "uf":"mg",
#             "is_staff": True
# }