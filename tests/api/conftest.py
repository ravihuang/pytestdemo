# -*- coding: utf-8 -*-
import functools
import requests
import json
from lxml import etree as et
from libs import excel
from tests.api import *

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

