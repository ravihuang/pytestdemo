# -*- coding: utf-8 -*-
'''
Created on 2017年4月28日
httpbin接口

@author: 黄小勇
'''
from .methods import *

data_basic_auth = [
    ("user","passwd",200),
    ("baduser","passwd",401),
    ("user","badpasswd",401),
]
@pytest.mark.parametrize("uname,passwd,status_code", data_basic_auth)
def test_basic_auth(uname,passwd,status_code):
    log.info("http 基本认证：")
    sc,h,body = get('http://httpbin.org/basic-auth/user/passwd', auth=(uname, passwd))
    assert sc==status_code 
       
def test_query_params():
    log.info( "http查询参数，Accept：")
    sc,h,body = get("http://httpbin.org/response-headers",params="Accept=ggg")    
    assert sc==200
    assert "content-type" in h
       
def test_query_data():
    log.info( "http查询数据，Accept：")
    sc,h,body = get("http://httpbin.org/response-headers",data="Accept=ggg")    
    assert sc==200
    assert "content-type" in h
      
def test_query_json():
    log.info("http查询json")
    sc,h,body = get_json("http://httpbin.org/response-headers",data={"Accept":"ggg"})    
    assert sc==200
    assert "content-type" in h
     
def test_xml():
    sc,h,body = get("http://httpbin.org/xml")    
    assert sc==200
    assert 1 == len(body.xpath('/slideshow/@title'))
    assert body.xpath('/slideshow/@title')[0].find("Slide" )>=0
     
def test_IMS():
    log.info("%s http带If-Modified-Since头返回304：" % cfg['PREFIX'])
    headers = {'If-Modified-Since':'Wed, 02 May 2012 18:32:20 GMT'}
    sc,h,body = get("http://httpbin.org/cache",headers=headers)    
    assert sc==304
     
def test_INM():
    log.info("%s http带If-None-Match头返回304 :" % cfg['PREFIX'])
    headers = {"If-None-Match":"231932131232103"}
    sc,h,body = get("http://httpbin.org/cache",headers=headers)    
    assert sc==304


data = read_excel('testdata/testcases.xlsx')
@pytest.mark.parametrize("edata", data)
def test_excel(edata):    
    log.info("执行测试用例{}--{}:".format(edata['ID'], edata['Desc']))
    log.info("第1步. 发送请求{} to /{}:".format(edata['Method'], edata['URL']))    
    url="http://httpbin.org/" +edata["URL"]
    if(edata['Method'] == 'GET'):
        sc,h,body = get(url)
    elif (edata['Method'] == 'PUT'):
        sc,h,body = put(url)
    elif (edata['Method'] == 'POST'):
        sc,h,body = post(url)
    elif (edata['Method'] == 'DEL'):
        sc,h,body = delete(url)     
        
    log.info("第2步. 确认收到的响应码为{}:".format(edata['Statuscode']))   
    assert sc == int(edata['Statuscode'])