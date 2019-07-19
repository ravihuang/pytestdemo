# -*- coding: utf-8 -*-
import sys
from .conftest import *

def read_excel(fname):
    return excel.read_sheet_byindex(fname=fname)

def dec_url(func):
    '''
          自动补全url
          自动处理json数据
         返回(响应码,headers,body)          
    '''    
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        fname=func.__name__
        if args[0].startswith('/'):
            args=list(args)
            args[0]=cfg['BASE_URL']+args[0]
            args=tuple(args)

        if "json" in fname:
            kwargs['data']=json.dumps(kwargs['data'])
            if('headers' not in kwargs):
                kwargs.setdefault('headers',{'Content-Type':'application/json;charset=UTF-8'})
            elif 'Content-Type' not in kwargs['headers']:
                kwargs['headers'].setdefault('Content-Type','application/json;charset=UTF-8')
        
            return func(*args,**kwargs)    
        resp = func(*args,**kwargs)
        headers= resp.headers 
        body = None
        if "Content-Type" in headers:
            if 'json' in headers['Content-Type'] and len(resp.text)>2:
                body=json.loads(resp.text)
            elif 'xml' in headers['Content-Type']:
                body=et.XML(resp.text.encode("utf-8"))
                              
        return resp.status_code,headers,body
    return wrapper

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
