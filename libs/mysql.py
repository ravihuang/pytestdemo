#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql

class mysql:
    def __init__(self,cfg):
        # 打开数据库连接
        self.db=pymysql.connect(cfg['DB_IP'],cfg['DB_USER'],cfg['DB_PASSWD'],cfg['DB'])
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor=self.db.cursor()
        
    def  __del__( self ):
        # 关闭数据库连接
        self.cursor.close()
        self.db.close()
                                                        
    def query_one_from(self,table):        
        # 使用 execute()  方法执行 SQL 查询 
        self.cursor.execute("SELECT * from "+table )    
        # 使用 fetchone() 方法获取单条数据.
        return self.cursor.fetchone()    
        
    def query_one_all_from(self,table):        
        self.cursor.execute("SELECT * from "+table )    
        return self.cursor.fetchall()    
        
    def drop_table(self,table):             
        self.cursor.execute("drop table "+table )    
   