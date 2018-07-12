# -*- coding: utf-8 -*-
import pytest
import falcon
from tests import *
from webtest import http

HTTP_200=falcon.HTTP_200

def pytest_collection_modifyitems(items):
    for item in items:
        if "test_" in item.nodeid:
            item.add_marker(pytest.mark.test)

            
@pytest.fixture(scope="session",autouse=True)
def setup_session(request):
    global app
    app = falcon.API()
    server =http.StopableWSGIServer.create(app, port=config.STUB_PORT,host='0.0.0.0')
    
    def teardon_session():
            server.shutdown()
    request.addfinalizer(teardon_session)
  
def add_route(uri_template, resource, *args, **kwargs):
    app.add_route(uri_template, resource, *args, **kwargs)
