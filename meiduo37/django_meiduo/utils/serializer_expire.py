from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData

from django_meiduo import settings


class SerializerExpire:
    serializer = Serializer(settings.SECRET_KEY, expires_in=3600)

    @classmethod
    def load_data(cls, data):
        try:
            return cls.serializer.loads(data)
        except BadData:
            return None
