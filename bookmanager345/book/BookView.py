#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : BookView.py
# @Author: ly
# @Date  : 2019/2/20
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from .views import login_required


class LoginRequiredMix:

    @classmethod
    def as_view(cls, **kwargs):
        view = login_required(super().as_view(**kwargs))
        return view


# @method_decorator(login_required, name='get')
class BookView(LoginRequiredMix, View):

    def get(self, req):
        return HttpResponse('This is get req ')


    def post(self, req):
        return HttpResponse('This is post req ')

    def put(self, req):
        return HttpResponse('This is put req ')

    def delete(self, req):
        return HttpResponse('This is delete req ')


