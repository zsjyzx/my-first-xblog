#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse

# 默认开启了csrf保护机制，本服务仅作自测使用，加上csrf_exempt去除掉csrf保护
@csrf_exempt
def fake_query(request):
    print('get into fake_query')
    dct = {
            'fake': 'test',
            'GET': request.GET,
            'POST': request.POST,
            'body': request.body,
            }
    try:
        dct['json_parsed_body'] = json.loads(request.body)
    except Exception as e:
        print('json loads except:{}'.format(e))
    return HttpResponse(HttpResponse(json.dumps(dct)), content_type='application/json')

