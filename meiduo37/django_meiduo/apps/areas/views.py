from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_extensions.cache.mixins import CacheResponseMixin
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from areas.models import Area, Address
from areas.serializers import AreaSerializer, AreaViewSetSerializer, SubViewSetSerializer, AddressModelSerializers, \
    AddressUpdateModelSerializer


# class AreaViewSet(ReadOnlyModelViewSet):
#     # TODO: 思路
#     # 1. 使用原始 apiview 查询采用 filter 参数查询省市区数据
#     # 2. 使用 serializer 配合 viewset 查询省市区数据
#     # 通过 get 请求传参方式很容易实现，只需要根据请求中的 id 当做parent_id 去查询即可, 但是路径/xx/xx 方式需要多个视图集?
#     # 此处选用第二种方案，第一种方案难度偏低
#     serializer_class = AreaSerializer
#     queryset = Area.objects.filter(pk=1)


class AreaApiView(APIView):

    def get(self, req, pk):
        pk = pk if pk else None
        areas = Area.objects.filter(parent_id=pk)
        serializer_class = AreaSerializer(instance=areas, many=True)
        return Response(serializer_class.data)


class AreaModelViewSet(CacheResponseMixin, ReadOnlyModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent_id=None)
        else:
            return Area.objects

    def get_serializer_class(self):
        """通过 不同的 Serializer 控制返回数据"""
        if self.action == 'list':
            return AreaViewSetSerializer
        else:
            return SubViewSetSerializer


class AddressModelViewSet(ModelViewSet):
    queryset = Address.objects

    # serializer_class = AddressModelSerializers

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'update':
            return AddressUpdateModelSerializer
        else:
            return AddressModelSerializers
