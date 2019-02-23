#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : middlesware.py
# @Author: ly
# @Date  : 2019/2/21



def middleware1(get_response):
    print('mid1: 此处代码初始化前执行一次')
    def middleware(req):
        print('mid1: 处理视图请求前执行')
        res = get_response(req)
        print('mid1: 处理视图请求后执行')
        return res
    return middleware


def middleware2(get_response):
    print('mid2: 此处代码初始化前执行一次')
    def middleware(req):
        print('mid2: 处理视图请求前执行')
        res = get_response(req)
        print('mid2: 处理视图请求后执行')
        return res
    return middleware
