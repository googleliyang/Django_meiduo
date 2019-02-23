#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : view_apiviews.py
# @Author: ly
# @Date  : 2019/2/22

import json

from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import PeopleInfo
from people.people_serializer import PeopleSerializer


class PeopleInfoViewSerializer(APIView):

    filter_fields = ['id','name']


    def get(self, req):
        peoples = PeopleInfo.objects.all()
        serializer = PeopleSerializer(instance=peoples, many=True)
        return Response(data=serializer.data)

    def post(self, req):
        params = json.loads(req.body.decode())
        data = {
            'name': params.get('name'),
            'description': params.get('description'),
            'book': params.get('book')
        }
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse('http validate ok')
        else:
            return JsonResponse(data = serializer.errors)


class PeopleInfoViewDetailSerializer(APIView):
    def get(self, req, id):
        try:
            people = PeopleInfo.objects.get(pk=id)
        except PeopleInfo.DoesNotExist:
            return HttpResponse(status=400)
        serializer = PeopleSerializer(instance=people)
        return JsonResponse(data=serializer.data)

    def put(self, req, id):
        try:
            people = PeopleInfo.objects.get(pk=id)
        except PeopleInfo.DoesNotExist:
            return HttpResponse(status=400)
        params = json.loads(req.body.decode())
        # TODO: update 时 data 怎么写, 老师用的 manager shell 自己写的 data 类
        data = {
            'name': params.get('name'),
            'description': params.get('description'),
            'book': params.get('book')
        }

        serializer =  PeopleSerializer(instance=people, data=data)
        if serializer.is_valid(raise_exception=True):
            # Restful serializer 如何返回数据
            data = serializer.save()
            print(data)
            return JsonResponse(data=serializer.data)
        else:
            return HttpResponse('验证失败')

    def delete(self, req, id):
        try:
            people = PeopleInfo.objects.get(pk=id)
        except PeopleInfo.DoesNotExist:
            return HttpResponse('未找到')
        people.delete()
        return HttpResponse(status=204)