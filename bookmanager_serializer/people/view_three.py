#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : view_three.py
# @Author: ly
# @Date  : 2019/2/23
from pymysql import DatabaseError
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView

from book.models import PeopleInfo
from .people_serializer import PeopleSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework.pagination import PageNumberPagination


class customPagi(PageNumberPagination):
    page_size = 2,
    page_query_param = 'pn'
    page_size_query_param = 'size'


class PeopleInfoThree(ListCreateAPIView):
    queryset = PeopleInfo.objects
    serializer_class = PeopleSerializer
    filter_fields = ['id','name']
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    # ordering_fields = ['id', 'readcount', 'commentcount']
    pagination_class = customPagi

class PeopleInfoDetailThree(RetrieveUpdateDestroyAPIView):
    queryset = PeopleInfo.objects
    serializer_class = PeopleSerializer


