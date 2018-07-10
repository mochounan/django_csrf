#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  :  nan
# @File     : csrf_.py


class DisableCSRF(object):
    """不执行csrf检查"""
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
