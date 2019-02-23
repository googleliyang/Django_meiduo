#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : view_generic_api_view.py
# @Author: ly
# @Date  : 2019/2/23
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from book.models import PeopleInfo
from people.people_serializer import PeopleSerializer
from rest_framework import status


class PeopleGenericApiView(GenericAPIView):
    queryset = PeopleInfo.objects.all()
    serializer_class = PeopleSerializer

    def get(self, req):
        return Response(self.get_serializer(instance=self.get_queryset(), many=True).data)

    def post(self, req):
        data = req.data
        print(data)
        serializer = self.get_serializer(data=data)
        # 因为抛出异常了，就不if判断了
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DetailPeopleGenericApiView(GenericAPIView):

    queryset = PeopleInfo.objects.all()
    serializer_class = PeopleSerializer

    def get(self, req, pk):
        return Response(self.get_serializer(instance=self.get_object()).data)

    def put(self, req, pk):
        serializer = self.get_serializer(instance=self.get_object(), data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, req, pk):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


