# -*- coding: utf-8 -*-

import pytest
from tests import *
import pymysql
from selenium import webdriver

config = {
          'host':cfg['DB_IP'],
          'port':cfg['DB_PORT'],
          'user':cfg['DB_USER'],
          'password':cfg['DB_PASSWD'],
          'db':cfg['DB'],          
          }
db = pymysql.connect(**config)
cursor = db.cursor()
driver = webdriver.Chrome()
url="http://%s/mt" % config['host']

@pytest.fixture(scope="session",autouse=True)
def setup_session(request):
    driver.implicitly_wait(0)
    driver.maximize_window()    
    driver.get(url)  
    def teardon_session():
            driver.quit()
            db.close()
            
    request.addfinalizer(teardon_session)
