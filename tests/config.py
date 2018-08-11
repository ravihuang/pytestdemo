# -*- coding: utf-8 -*-
#SUT IP地址
HOST="192.168.117.133"

cfg={
    'BASE_URL':"http://%s/mt" % HOST,
    'PREFIX':"",
    'S':None,
    'DB_IP':HOST,
    'DB_PORT':3306,
    'DB_USER':'tester',
    'DB_PASSWD':'passwd',
    'DB':'scott',    
}

#STUB服务器端口号
STUB_PORT=8090
