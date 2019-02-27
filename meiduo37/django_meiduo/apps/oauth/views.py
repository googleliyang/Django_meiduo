from django.shortcuts import render
from QQLoginTool.QQtool import OAuthQQ
from .serializers import AuthUserSerializer
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_meiduo import settings

import logging

# 获取在配置文件中定义的logger，用来记录日志
from oauth.models import OAuthQQUser
from users.models import User
from utils.users import generate_save_user_token, get_token_by_jwt

logger = logging.getLogger('meiduo')

oauth = OAuthQQ(client_id=settings.QQ_CLIENT_ID, client_secret=settings.QQ_CLIENT_SECRET,
                redirect_uri=settings.QQ_REDIRECT_URI, state=next)


class QQAuthURLView(APIView):

    def get(self, req):
        login_url = oauth.get_qq_url()
        state = req.query_params.get('state')
        if not state:
            state = '/'
        return Response({'auth_url': login_url})


class QQAuthUserView(APIView):
    """此处接收用户认证完后回调的前端绑定页面, 页面将 code 传递过来，根据code值去生成认证的信息"""

    def get(self, req):
        code = req.query_params.get('code')
        if not code:
            return Response({'message': '缺少codeId'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            access_token = oauth.get_access_token(code)
            open_id = oauth.get_open_id(access_token)
        except Exception as e:
            logger.error(e)
            return Response({'message': 'QQ服务器异常'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        # 使用 openId 绑定的用户Id
        try:
            oauth_user = OAuthQQUser.objects.get(openId=open_id)
        except OAuthQQUser.DoesNotExist:
            access_token_openid = generate_save_user_token(open_id)
            return Response({'access_token': access_token_openid})
        else:
            # 如果绑定美多账户
            # 帮他登录返回用户数据即可
            # user = User.objects.get(pk=user.user_id)
            user = oauth_user.user
            token = get_token_by_jwt(user)
            res_data = {
                'username': user.username,
                'user_id': user.user_id,
                'token': token
            }
            return Response(res_data)

    def post(self, req):
        # 获取 手机号，验证码，access_token
        # 验证通过后帮用户注册
        # 写入 oauth 表中
        serializer = AuthUserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        user = User()
        user.mobile = req.data.get('mobile')
        user.set_password(req.data.get('password'))
        try:
            #TODO://  应该用事务, 并且移动到 validate 里操作
            if user.save():
                serializer.save()
        except Exception as e:
            logger.error(e)
