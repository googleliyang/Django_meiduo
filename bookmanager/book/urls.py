#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ly
# @Date  : 2019/2/13

from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^index$', index),
    url(r'^lazy/(?P<id>\d+)/(?P<name>\w+)$', lazy),
    url(r'^query$', query, name='query')
]
