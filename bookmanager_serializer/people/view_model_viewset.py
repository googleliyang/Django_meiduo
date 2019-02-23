#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : view_model_viewset.py
# @Author: ly
# @Date  : 2019/2/23
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.models import PeopleInfo
from .people_serializer import PeopleSerializer


class PeopleInfoModelViewSet(ModelViewSet):
    queryset = PeopleInfo.objects
    serializer_class = PeopleSerializer

    @action(methods=['GET'], detail=True)
    def lala(self, req, pk):
        return Response('ok' + pk)
        pass

