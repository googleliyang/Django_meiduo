import re

from rest_framework_jwt.settings import api_settings

from django_meiduo import settings
from users.models import User
from django.contrib.auth.backends import ModelBackend
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User.

    Example:

    def jwt_response_payload_handler(token, user=None, request=None):
        return {
            'token': token,
            'user': UserSerializer(user, context={'request': request}).data
        }

    """
    return {
        'token': token,
        'username': user.username,
        'user_id': user.id
    }


def get_user_by_account(account):
    try:
        if re.match(r'1[345789]\d{9}', account):
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        user = None
    return user


class UsernameMobileAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            return user


def generate_save_user_token(openId):
    serializer = Serializer(settings.SECRET_KEY, expires_in=3600)
    data = {'openid': openId}
    token = serializer.dump(data)
    return token.decode()

#
# def get_check_user_token(access_token):
#     serializer = Serializer(settings.SECRET_KEY, expires_in=3600)
#     token = None
#     try:
#         token = serializer.loads(access_token)
#     except BadData as e:
#         print('BadData error %s' % e)
#     return token


def get_token_by_jwt(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token
