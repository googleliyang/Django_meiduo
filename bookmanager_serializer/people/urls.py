#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ly
# @Date  : 2019/2/22

from django.conf.urls import url
from .views import PeopleInfoView, PeopleInfoDetail
from .view_serializer import PeopleInfoViewSerializer, PeopleInfoViewDetailSerializer
from .view_apiviews import PeopleInfoViewSerializer as ApiViewPeopleInfoViewSerializer, PeopleInfoViewDetailSerializer as ApiViewPeopleInfoViewDetailSerializer
from .view_generic_api_view import PeopleGenericApiView, DetailPeopleGenericApiView
from .view_mix import PeopleInfoMix, PeopleInfoDetailMix
from .view_three import PeopleInfoThree, PeopleInfoDetailThree
from .view_viewset import PeopleInfoViewSet
from .view_model_viewset import PeopleInfoModelViewSet



urlpatterns = [
    # 普通View 使用 Serializer 方法
    url(r'people/$', PeopleInfoView.as_view()),
    # localhost:8000/people/people
    url(r'people/(?P<id>\d+)$', PeopleInfoDetail.as_view()),

    # APiviewView 使用 Serializer 方法
    url(r'peoples/$', PeopleInfoViewSerializer.as_view()),
    url(r'peoples/(?P<id>\d+)$', PeopleInfoViewDetailSerializer.as_view()),

    # 使用apivew 和 view 基本一样 但是带哟特殊 request response
    url(r'peoplea/$', ApiViewPeopleInfoViewSerializer.as_view()),
    url(r'peoplea/(?P<id>\d+)$', ApiViewPeopleInfoViewDetailSerializer.as_view()),

    # 使用generic apivew 和 apiview 基本一样, 但是抽取了 queryset 和 serializer, 不用每个方法里都写了
    url(r'peopleg/$', PeopleGenericApiView.as_view()),
    url(r'peopleg/(?P<pk>\d+)$', DetailPeopleGenericApiView.as_view()),

    # 使用generic 带有 mix
    url(r'peoplem/$', PeopleInfoMix.as_view()),
    url(r'peoplem/(?P<pk>\d+)$', PeopleInfoDetailMix.as_view()),

    # 三级视图, 父类已经实现了 get put post delete 方法 只需要继承 传递 ,query set , 不需要写 get put post delete 方法了
    url(r'peoplet/$', PeopleInfoThree.as_view()),
    url(r'peoplet/(?P<pk>\d+)$', PeopleInfoDetailThree.as_view()),

    # 视图集(知道了 django.shrot... get_object_or_404 方法), 使用和 apiview + serializer 没有区别
    # 因为继承自了 Apivew
    url(r'peoplev/$', PeopleInfoViewSet.as_view({'get': 'list'})),
    url(r'peoplev/(?P<pk>\d+)$', PeopleInfoViewSet.as_view({'get': 'retrieve'})),

]

# modelViewSet 实现了增删改查只需要设置，querySet 和 serialize 就可以了, 而且还带 web 页面!
# 可以使用 @action 给试图集补充方法
# 视图集高度封装有很多的局限性
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'peoplemv', PeopleInfoModelViewSet)
urlpatterns += router.urls

# 二级视图也没讲，和 自己体会吧和 genericApiView..基本一样
