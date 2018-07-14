# -*- coding: utf-8 -*-
'''
Created on 2017年4月28日
订单接口

@author: 黄小勇
'''
from methods import *

def test_get():  
    print "test_get"  
    sc,h,body= get("/orders")
    assert sc==200
    assert len(body)>0
    assert h['Content-type'].index("json")>0
    assert h.get('user-agent1') == None
    
def test_post():
    print "test_post"
    form = {"name": "iphone", 
            "quantity": 1111
    }    
    sc,h,body = post_json("/orders", data=form)
    global location
    location=h['Location']
    assert sc==201
    
@pytest.mark.dependency(depends=["test_post"])
def test_put():
    print "test_put"
    form = {"name": "abc", 
            "quantity": 222,
            "version":0
    }
    sc,h,body = put_json(location, data=form)
    assert sc==204