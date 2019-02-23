#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ly
# @Date  : 2019/2/22

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BookView

router = DefaultRouter()
router.register(r'books', BookView, base_name='')
urlpatterns = [
    url(r'^', include(router.urls))
]
# urlpatterns += router.urls

