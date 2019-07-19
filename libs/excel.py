#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=PendingDeprecationWarning)
    import xlrd

from tests import *

def open_excel(fname='../testcases.xlsx'):
    try:
        data = xlrd.open_workbook(fname, encoding_override='utf-8')
        return data
    except Exception as e:
        log.error(str(e))
# 根据索引获取Excel表格中的数据   参数:file：Excel文件路径     
# colnameindex：表头列名所在行的所以 ，by_index：表的索引
def read_sheet_byindex(fname='../testcases.xlsx', colnameindex=0, by_index=0):
    data = open_excel(fname)
    table = data.sheets()[by_index]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    colnames = table.row_values(colnameindex)  # 某一行数据 
    list = []
    for rownum in range(1, nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

# 根据名称获取Excel表格中的数据   参数:fname：Excel文件路径     
# colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def read_sheet_byname(fname='../testcases.xlsx', colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(fname)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows  # 行数 
    colnames = table.row_values(colnameindex)  # 某一行数据 
    list = []
    for rownum in range(1, nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():
   tables = read_sheet_byindex()
   for row in tables:
       log.info(json.dumps(row, encoding='UTF-8', ensure_ascii=False))

   tables = read_sheet_byname()
   for row in tables:
       log.info(json.dumps(row, encoding='UTF-8', ensure_ascii=False))

if __name__ == "__main__":
    main()
