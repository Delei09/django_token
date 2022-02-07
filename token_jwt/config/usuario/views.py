from rest_framework.views import Response , APIView
from rest_framework import authentication , permissions

class HelloApiview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response("Olá Mundo")