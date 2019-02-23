#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : BookInfoSerializer.py
# @Author: ly
# @Date  : 2019/2/21
from rest_framework import serializers

from book.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'


