from random import randint

from django.http import HttpResponse
from django_redis import get_redis_connection
# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from libs.captcha.captcha import captcha
from . import constants
from .serializers import RegisterSmsSerializer


class SmsImgCodeApiView(APIView):

    def get(self, req, img_code_id):
        redis_conn = get_redis_connection(constants.REDIS_CODE)
        captcha_code, img = captcha.generate_captcha()
        # 放入 redis 设置  60s 过期时间
        redis_conn.setex('img_%s' % img_code_id, constants.SMS_IMAGE_CODE_EXPIRE_TIME, captcha_code)
        return HttpResponse(img, content_type='image/jpeg')


class RegisterSmsApiView(GenericAPIView):
    serializer_class = RegisterSmsSerializer

    def get(self, req, mobile):
        serializer = self.get_serializer(data=req.query_params)
        serializer.is_valid(raise_exception=True)
        redis_conn = get_redis_connection(constants.REDIS_CODE)
        sms_flag = constants.SMS_CODE_FLAG % mobile
        sms_code_flag = constants.SMS_CODE_FLAG % mobile
        if redis_conn.get(sms_flag):
            return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)

        # 生成短信验证码
        sms_code = '%06d' % randint(0, 99999)
        redis_conn.setex(sms_code_flag, 60 * 5, 1)
        redis_conn.setex(sms_flag, constants.SMS_INTERVAL, sms_code)
        from celery_tasks.sms.tasks import send_sms_code
        send_sms_code.delay(mobile, sms_code)
        # ccp = CCP()
        # ccp.send_template_sms(mobile, [sms_code, 5], 1)
        return Response({'message': 'ok'})
