#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : view_viewset.py
# @Author: ly
# @Date  : 2019/2/22
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from book.models import PeopleInfo
from .people_serializer import PeopleSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PeopleInfoViewSet(ViewSet):
    filter_fields = ['id','name']
    def list(self, req):
        qSet = PeopleInfo.objects.all()
        serializer = PeopleSerializer(instance=qSet, many=True)
        return Response(data=serializer.data)

    def retrieve(self, req, pk):
        qSet = PeopleInfo.objects.all()
        people = get_object_or_404(qSet, pk=pk)
        serializer = PeopleSerializer(instance=people)
        return Response(serializer.data)


