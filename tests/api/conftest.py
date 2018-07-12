# -*- coding: utf-8 -*-
import functools
import pytest
import requests
from tests import cfg
import json
from lxml import etree as et
from libs import excel
 
_module_id=0
_case_id=0

def pytest_collection_modifyitems(items):
    for item in items:
        if "test_" in item.nodeid:
            item.add_marker(pytest.mark.test)

            
@pytest.fixture(scope="session",autouse=True)
def setup_session(request):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}    
    cfg['S']=requests.Session()
    cfg['S'].headers.update(headers)
    def teardon_session():
            pass
    request.addfinalizer(teardon_session)
  
@pytest.fixture(scope="module",autouse=True)
def setup_module(request):
    global _module_id, _case_id
    _module_id+=1     
    _case_id=0       
    def teardown_module():
            pass
    request.addfinalizer(teardown_module)
  
@pytest.fixture(scope="function",autouse=True)
def setup_function(request):
    global _case_id
    _case_id+=1        
    print("\n")
    cfg['PREFIX']="%s.%s" % (_module_id,_case_id)
    def teardown_function():
            pass
    request.addfinalizer(teardown_function) 

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