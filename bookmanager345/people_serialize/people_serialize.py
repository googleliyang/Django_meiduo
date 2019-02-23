#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : people_serialize.py
# @Author: ly
# @Date  : 2019/2/21)
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import  ModelSerializer

from book.BookInfoSerializer import BookInfoSerializer
from book.models import PeopleInfo


class PeopleSerialize(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='Name', max_length=10)
    # book = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
    # book = serializers.StringRelatedField(label='图书', read_only=False)
    # book = BookInfoSerializer()


class PeopleViewSerializer(ModelSerializer):
    class Meta:
        model = PeopleInfo
        fields = '__all__'

