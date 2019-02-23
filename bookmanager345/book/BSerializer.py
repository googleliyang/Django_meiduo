#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : BSerializer.py
# @Author: ly
# @Date  : 2019/2/21
from rest_framework import serializers
from people_serialize import people_serialize
class BSerializer(serializers.Serializer):
    name = serializers.CharField(label='图书')
    # peopleinfo_set = serializers.StringRelatedField(read_only=True, many=True)
    peopleinfo_set = people_serialize.PeopleSerialize(read_only=True, many=True)

