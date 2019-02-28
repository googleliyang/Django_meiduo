from rest_framework.serializers import Serializer, ModelSerializer

from areas.models import Area, Address


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


class AddressModelSerializers(ModelSerializer):
    class Meta:
        model = Address
        # fields = '__all__'
        exclude = ['user']

    def create(self, validated_data):
        # todo: set from jwt
        user_id = validated_data.get('user').id
        validated_data['user_id'] = user_id
        return Address.objects.create(**validated_data)


class AddressUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = Address
        exclude = ['user']
        extra_kwargs = {
            'detail_address': {'required': False},
            'mobile': {'required': False},
            'username': {'required': False},
            'email': {'required': False},
            'telephone': {'required': False},
            'is_default': {'required': False},
            'area': {'required': False},
        }

    def update(self, instance, validated_data):
        # TODO: ISSUE, 这样写太浪费时间且为重复工作，但是简单一搜也没有找到替换写的方式，都会面临这样的问题
        # 而一旦开始写的思路错了，后边将会遇到很多难解的问题， 如这个 ModelViewset 自动调用的create 方法如何拿到用户
        # 难不成要重写 post
        """添加时验证所有字段，可是修改时不需要验证所有字段啊，modelViewSet 如何区分"""
        # 方式一 如 省市区一样，两个 serializer, 根据 self.action 进行选用
        instance.is_default = validated_data.get('is_default', instance.is_default)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.email = validated_data.get('email', instance.email)
        instance.area_id = validated_data.get('area_id', instance.area_id)
        instance.save()
        return instance
