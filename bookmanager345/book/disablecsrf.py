#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : disablecsrf.py
# @Author: ly
# @Date  : 2019/2/22

class DisableCSRF(object):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
