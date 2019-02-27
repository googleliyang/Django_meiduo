from redis import RedisError
from rest_framework import serializers
from django_redis import get_redis_connection
import logging

from verifications import constants

logger = logging.getLogger('meiduo')


class RegisterSmsSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    text = serializers.CharField(max_length=4, min_length=4, required=True, label="用户输入验证码")
    image_code_id = serializers.CharField(required=True, label='验证码唯一性 ID')

    def validate(self, attrs):
        text = attrs.get('text')
        image_code_id = attrs.get('image_code_id')
        redis_conn = get_redis_connection(constants.REDIS_CODE)
        redis_img_key = constants.IMG_CODE_PREFIX % image_code_id
        redis_text = redis_conn.get(redis_img_key)
        if redis_text is None:
            raise serializers.ValidationError('验证码已过期')
        try:
            redis_conn.delete(redis_img_key)
        except RedisError as e:
            logging.error(e)
            raise serializers.ValidationError('redis 错误')
        if redis_text.decode().lower() != text.lower():
            raise serializers.ValidationError('验证码错误')
        return attrs
