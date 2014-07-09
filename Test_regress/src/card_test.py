# -*- coding: UTF-8 -*-
'''
Created on Jun 1, 2012

@author: yilulu
'''
import unittest, card_management, login, xlrd,random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import login, course_management, student_management, card_management,cate_management,admin_management,user_management
import time, ConfigParser

def test_card():
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    test_enviroment = 'omega'
    base_url = "http://www."+test_enviroment+".ablesky.com/"
    
    user_name = 'ibm'
    user_psw = '1234' 
    org_name = user_name
    
    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)
    
    login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)     
    card = xlrd.open_workbook('D:\\PaymentCardList-201210221522.xls' )     
    table = card.sheet_by_index(0) 
            #list_ran = []
            #for ran in range(1002):
             #   rand_num = random.randint(2,40001)
              #  list_ran.append(rand_num)
            
    for j in range(1002):
        if j < 2:
            continue
        card_num = table.cell(j,0).value
        card_psw = table.cell(j,1).value 
        try:
            card_management.use_prepaid_card(cfg, driver, base_url, card_num, card_psw)
        except:
            print card_num,card_psw
                    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    test_card()