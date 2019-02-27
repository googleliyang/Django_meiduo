import re

from rest_framework import serializers
from django_redis import get_redis_connection
from rest_framework_jwt.settings import api_settings

from users.models import User

# 有模型需要保存至模型情况下使用 ModelSerializer
from utils.users import get_token_by_jwt
from verifications import constants as verify_constants


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=20, min_length=8, label='确认密码', write_only=True)
    # 短信验证码拿来验证
    sms_code = serializers.CharField(max_length=6, min_length=6, label='短信验证码', write_only=True)
    allow = serializers.CharField(label='是否同意协议', write_only=True)
    token = serializers.CharField(label='登录状态token', read_only=True)  # 增加token字段

    class Meta:
        model = User
        fields = ['username', 'mobile', 'password', 'allow', 'password2', 'sms_code', 'token']
        extra_kwargs = {
            id: {'read_only': True},
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名',
                },
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }

    def validate_mobile(self, value):
        if not re.match(r'1[345789]\d{9}', value):
            raise serializers.ValidationError('用户密码不符合格式')
        return value

    def validate_allow(self, value):
        # 注意,前段提交的是否同意,我们已经转换为字符串
        if value != 'true':
            raise serializers.ValidationError('您未同意协议')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        mobile = attrs.get('mobile')
        client_sms_code = attrs.get('sms_code')
        if password != password2:
            raise serializers.ValidationError('两次密码输入不一致')
        redis_conn = get_redis_connection(verify_constants.REDIS_CODE)
        redis_sms_code = redis_conn.get(verify_constants.SMS_CODE_PREFIX % mobile)
        if redis_sms_code is None:
            raise serializers.ValidationError('验证码已过期')
        if client_sms_code != redis_sms_code.decode():
            raise serializers.ValidationError('验证码错误')
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        del validated_data['sms_code']
        del validated_data['allow']
        password = validated_data['password']
        # 存在 super().create 成功密码修改不成功的情况
        # 存在写入成功读取数据失败的情况，但此时用户已经注册成功，这样则影响实际注册结果
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        token = get_token_by_jwt(user)
        user.token = token

        return user
