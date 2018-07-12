# -*- coding: utf-8 -*-
import sys
from conftest import *

def delete(url,**kwargs):    
    return cfg['S'].delete(url,**kwargs)

def delete_json(url, data=None, **kwargs):
    return delete(url,data=data,**kwargs)    

def get(url,**kwargs):    
    return cfg['S'].get(url,**kwargs)

def get_json(url, data=None, **kwargs):
    return get(url,data=data,**kwargs)    

def post(url, data=None, **kwargs):
    return cfg['S'].post(url, data,**kwargs)    
    
def post_json(url, data=None, **kwargs):
    return post(url, data=data,**kwargs)    
    
def put(url, data=None, **kwargs):
    return cfg['S'].put(url, data,**kwargs)    

def put_json(url, data=None, **kwargs):
    return put(url, data=data,**kwargs)   

def wrap_methods( cls, wrapper ):
    for key, value in cls.__dict__.items( ):
        if hasattr( value, '__call__' ):
            setattr( cls, key, wrapper( value ) )
# 装饰list中的方法
[setattr(sys.modules[__name__],x.func_name,dec_url(x)) 
 for x in [delete,get,post,put,delete_json,get_json,post_json,put_json]]
