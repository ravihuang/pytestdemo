# -*- coding: utf-8 -*-

import os
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   # @UndefinedVariable

import logging.config
LOGCONF="conf"+os.sep+"logging.conf"
while not os.path.exists(LOGCONF) and LOGCONF.count("..")<5:
    LOGCONF=".."+os.sep+LOGCONF
logging.config.fileConfig(LOGCONF)
log = logging.getLogger('root')


import pytest
import pymysql
from time import sleep
from config import *

def wait_until_succeed(retry, retry_interval,func,*args,**kwargs):
    '''
    retry: 重试时间(秒)
    retry_interval：重试间隔时间(秒)
    func,*args,**kwargs: func(*args,**kwargs)
    '''
    import datetime
    starttime = datetime.datetime.now()
    while (datetime.datetime.now() - starttime).seconds<retry:
        try:
            func(*args,**kwargs)
            sleep(retry_interval)
            break
        except:
            pass