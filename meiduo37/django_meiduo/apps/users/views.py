# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_decode_handler
from .serializers import RegisterSerializer, BindEmailSerializer, UserInfoSerializer

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


class UserInfoApiView(APIView):

    def get(self, req):
        user = jwt_decode_handler(req._auth)
        user_id = user.get('user_id')
        user_obj = User.objects.get(pk=user_id)
        serializer = UserInfoSerializer(instance=user_obj)
        return Response(serializer.data)


class EmailApiView(APIView):

    def get(self, req):
        token = req.query_params.get('token')
        if not token:
            return Response({'message': '缺少token'}, status=status.HTTP_400_BAD_REQUEST)

        # 从token 中取出 user 数据
        # 修改为 激活状态
        # 保存并返回
        user = User.get_user_id_from_verify_token(token)
        user.email_active = True
        user.save()
        return HttpResponse({'msg': 'ok'})

    # 根据 jwt token 获取用户 实例
    def put(self, req):
        permission_classes = [IsAuthenticated]
        # token = req.META.get('Authorization')
        # 通过 debug 模式可以看到可以直接通过 self.request.user 获取 到 User 的模型类j
        user = jwt_decode_handler(req._auth)
        user_id = user.get('user_id')
        user_obj = User.objects.get(pk=user_id)
        serializer = BindEmailSerializer(instance=user_obj, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        from celery_tasks.email.tasks import send_email
        email_address = user_obj.generate_verify_email_address()
        send_email.delay(serializer.data.get('email'), email_address)
        return Response(data=serializer.data)
