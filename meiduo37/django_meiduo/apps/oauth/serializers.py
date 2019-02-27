from rest_framework import serializers
from utils.serializer_expire import  SerializerExpire
from oauth.models import OAuthQQUser
from verifications import constants
from utils.serializer_expire import SerializerExpire


class AuthUserSerializer(serializers.Serializer):
    # user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='用户')
    # openId = models.CharField(max_length=64, verbose_name='openid', db_index=True)
    access_token = serializers.CharField(max_length=64, label='openid')
    mobile = serializers.CharField(max_length=11, min_length=11, label='手机号')
    sms_code = serializers.CharField(max_length=6, min_length=6, label='验证码')

    def validate(self, attrs):
        # 参数为  手机号，验证码, access_token,
        # 检查验证码是否正确
        # 正确的话生成 token, 返回用户信息
        mobile = attrs.get('mobile')
        client_code = attrs.get('sms_code')
        access_token = attrs.get('access_token')
        # openid = get_check_user_token(access_token).openid
        openid = SerializerExpire.load_data(access_token).openid
        if openid is None:
            raise serializers.ValidationError('认证已过期')
        from django_redis import get_redis_connection
        redis_conn = get_redis_connection(constants)
        key = constants.SMS_CODE_PREFIX % mobile
        redis_code = redis_conn.get(key)
        if client_code.lower() != redis_code.decode().lower():
            raise serializers.ValidationError('验证码错误')

    def create(self, validated_data):
        access_token = validated_data.get('access_token')
        openid = SerializerExpire.load_data(access_token).openid
        # 验证通过之后，保存用户，应该是保存 生成注册用户，并保存 oauth 信息
        # 参数传递过来的
        user = validated_data('user')
        return OAuthQQUser.objects.create(user=user.id, openId=openid)

    def update(self, instance, validated_data):
        pass
