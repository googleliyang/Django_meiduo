#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ly
# @Date  : 2019/2/21

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

route = DefaultRouter()
route.register(r'peoples', views.PeopleViewSet)

urlpatterns = [
    url(r'^', include(route.urls)),
    # url(r'^people/(?P<id>\d+)$', views._PeopleInfo.as_view())
]
