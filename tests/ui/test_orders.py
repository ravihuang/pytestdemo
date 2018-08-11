#coding:utf-8
'''
Created on 2017

@author: huangxy
'''
from conftest import * 

def setup_module(module):    
    log.info("setup_module,清理脏数据")
    cursor.execute("TRUNCATE table order_item")
    
def teardown_module(module):
    log.info("teardown_module")
    #cursor.execute("TRUNCATE table order_item")
    
    
def test_case_01_01():
    assert u"接口测试及自动化测试" in driver.title
    log.info("2.点击自动化测试课程：")
    driver.find_element_by_link_text("自动化测试课程").click()
    
    log.info("3.输入产品及数量：")
    e = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "ProductName"))
    )
    e.send_keys("iphone")
    driver.find_element_by_name("Quantity").send_keys("1234") 
    
    log.info("4.点击提交按钮：")   
    driver.find_element_by_xpath("//*[@id='submitBtn']").click()
    
    log.info("5.确认提交成功：")
    log.info("5.1. 确认购物车记录正确：")
    iframe=driver.find_element_by_id("fra")
    driver.switch_to.frame(iframe)
    select=Select(driver.find_element_by_id('buy'))    
    wait_until_succeed(30,1,select.select_by_visible_text,u"产品:iphone,数量:1234")
    driver.switch_to.default_content()
    
    log.info("5.2. 确认提示信息正确：")
    rst=driver.find_element_by_id("msg").text
    assert rst==u"你购买了iphone，一共1234件。"
    
    log.info("5.3. 确认数据库记录正确：")
    cursor.execute("SELECT id from order_item where name='iphone' and quantity=1234" )
    print cursor.rowcount    
    assert cursor.fetchall()