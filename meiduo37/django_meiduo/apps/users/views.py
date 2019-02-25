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


# class RegisterCreateView(CreateAPIView):
#     serializer_class = RegisterSerializer

class RegisterCreateView(APIView):

    def post(self, req):
        data = req.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


