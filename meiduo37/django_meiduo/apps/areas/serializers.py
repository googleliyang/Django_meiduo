from rest_framework.serializers import Serializer, ModelSerializer

from areas.models import Area


class AreaSerializer(ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'


class AreaViewSetSerializer(ModelSerializer):

    class Meta:
        model = Area
        fields = ['id', 'name']


class SubViewSetSerializer(ModelSerializer):

    subs = AreaViewSetSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ['id', 'name', 'subs']

