#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : BookSerializer.py
# @Author: ly
# @Date  : 2019/2/22

from rest_framework import serializers

from book.models import BookInfo


class BookViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'


