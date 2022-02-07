from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication , permissions
from django.contrib.auth.models import User

class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self , request, format=None) :
        username = [user.username for user in User.objects.all()]
        return Response(username)
class CadastroUserApiview(APIView):
    def post(self, request, format=None):
        nome = request.data['name'] 
        emaill = request.data['email']
        password = request.data['senha']
        print(nome, emaill, password)
        user = User(
            username = nome,
            email = emaill,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        
        return Response(user.get_username)
