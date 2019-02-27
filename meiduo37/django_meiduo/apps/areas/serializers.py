from rest_framework.serializers import Serializer, ModelSerializer

from areas.models import Area


class AreaSerializer(ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'
