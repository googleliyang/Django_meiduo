#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : people_serializer.py
# @Author: ly
# @Date  : 2019/2/22

from rest_framework import serializers

from book.models import PeopleInfo, BookInfo


class PeopleSerializer(serializers.Serializer):
    # def __init__(self):
    #     print(123)
    #     pass
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    def custom_validate(value):
        raise serializers.ValidationError('我就是来捣乱的 %s' %value)

    id = serializers.IntegerField(label='id', read_only=True)
    name = serializers.CharField(max_length=20, label='名名', )# validators=[custom_validate]
    # gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = serializers.CharField(max_length=200,  label='描述信息', required=True)
    book = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
    # is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    gender = serializers.ChoiceField(choices=GENDER_CHOICES, default=0, label='性别')

    def create(self, validated_data):

        return PeopleInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 传递过来的对象，
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.book = validated_data.get('book', instance.book)
        instance.save()
        return instance
        # pass


    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('名字长度不可以低于5个字符')
        return value

    def validate(self, attrs):
        name = attrs['name']
        desc = attrs['description']
        if len(name) < len(desc):
            raise serializers.ValidationError('名称长度不可以小于评论')
        return attrs


