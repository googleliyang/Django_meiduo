from django.db import models
from django.contrib.auth.models import AbstractUser
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from utils.serializer_expire import SerializerExpire
# Create your models here.
from django_meiduo import settings
from users import constants


class User(AbstractUser):
    mobile = models.CharField(max_length=11, verbose_name='手机号', unique=True)
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def generate_verify_email_address(self):
        serializer = Serializer(settings.SECRET_KEY, constants.Email.VERIFY_EXPIRE)
        data = serializer.dumps({'user_id': self.id, 'email': self.email}).decode()
        return constants.Email.SUCCESS_VERIFY_CALLBACK_ADD % data

    @classmethod
    def get_user_id_from_verify_token(cls, token):
        res = SerializerExpire.load_data(token)
        user_id = res.get('user_id')
        user_mail = res.get('email')
        user = cls.objects.get(id=user_id, email=user_mail)
        return user
