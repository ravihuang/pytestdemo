# -*- coding: utf-8 -*-
import pytest
from mt import config as c

config = {
          'host':c.cfg['DB_IP'],
          'port':c.cfg['DB_PORT'],
          'user':c.cfg['DB_USER'],
          'password':c.cfg['DB_PASSWD'],
          'db':c.cfg['DB'],          
          }
HOST=c.HOST