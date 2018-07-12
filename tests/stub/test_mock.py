#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月14日

@author: 黄小勇
'''
import requests
from conftest import *

def test_things():
    class Things(object):
        def on_get(self, req, resp):
            """Handles GET requests"""
            resp.status = HTTP_200  # This is the default status
            resp.body = ('hello things!')
    # things will handle all requests to the '/things' URL path
    add_route('/things', Things())
    resp=requests.get("http://127.0.0.1:%s/things" % config.STUB_PORT)
    print resp.text

