# Create your views here.
from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer

from users.models import User


class RegisterUsernameApiView(APIView):

    def get(self, req, username):
        count = User.objects.filter(username=username).count()
        data = {
            'count': count,
            'username': username,
        }
        return Response(count)


class RegisterCreateView(CreateAPIView):
    serializer_class = RegisterSerializer


