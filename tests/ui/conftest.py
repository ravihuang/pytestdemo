# -*- coding: utf-8 -*-
from tests.ui import *

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
url=cfg["BASE_URL"]

@pytest.fixture(scope="session",autouse=True)
def setup_session(request):
    driver.implicitly_wait(0)
    driver.maximize_window()    
    driver.get(url)  
    def teardon_session():
            driver.quit()
            db.close()
            
    request.addfinalizer(teardon_session)
