# -*- coding: UTF-8 -*-

import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

from PO.base import Base
import login, card_management

class StudyCardTest(unittest.TestCase):


    def setUp(self):

        self.cfg_file = 'config.ini'
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(self.cfg_file)
        self.browser = self.cfg.get("env_para", "browser")
        self.org_name = self.cfg.get("env_para", "org_name")
        self.org_password = self.cfg.get("env_para", "org_password")
        self.user_name = self.cfg.get("env_para", "user_name")
        self.user_password = self.cfg.get("env_para", "user_password")
        self.base_url = self.cfg.get("env_para", "base_url")
        self.dbhost = self.cfg.get("env_para", "dbhost")

        if os.path.exists("C:\\test_rs_pic") != True:
                os.system("mkdir C:\\test_rs_pic")

        if self.browser == 'ie':
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver = webdriver.Chrome(chromedriver)
        elif self.browser == "Html":
            self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        else:
            self.driver = webdriver.Ie()

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get(self.base_url)

        cookie1 = self.cfg.get('env_para', 'cookie1')
        if(cookie1 == 'no'):
            login.login_by_logindo(self.cfg, self.driver, self.base_url, self.org_name, self.org_password)
            self.cfg.set("env_para", "cookie1", str(self.driver.get_cookie('ASUSS')['value']))
            self.cfg.write(open(self.cfg_file, "w"))
           
            #本来还有一个叫RM的cookie，但是值都是rm不变所以不取了
            # path=/; domain=.ablesky.com
        else:
            self.driver.add_cookie({'name':'ASUSS', 'value':cookie1, 'path':'/', 'domain':'.ablesky.com'})
            self.driver.add_cookie({'name':'RM', 'value':'rm'})

    #充值卡 
    def test_prepaid_cardgroup(self):#充值卡
        ba = Base(self.driver)
        title = u"prepaid" + ba.rand_name()
        price = 100
        #建卡组
        card_management.add_prepaid_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, group_name=title, group_price=price)
         
        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename        
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card()
            self.p_card_num = card_info[0]
            self.p_card_pwd = card_info[1]
            self.cfg.set("env_para", "p_card_num", self.p_card_num)
            self.cfg.set("env_para", "p_card_pwd", self.p_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))

    #添加卡组-充课卡   
    def test_course_cardgroup(self):
        ba = Base(self.driver)
        title = u"course" + ba.rand_name()
        card_management.add_course_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, group_name=title)

        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card(1)#充课卡需要传参数
            self.c_card_num = card_info[0]
            self.c_card_pwd = card_info[1]
            self.cfg.set("env_para", "c_card_num", self.c_card_num)
            self.cfg.set("env_para", "c_card_pwd", self.c_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))
        
     #添加卡组-补课卡         
    def test_cate_cardgroup(self):
        ba = Base(self.driver)
        title = u"cate" + ba.rand_name()
        card_management.add_cate_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, title)

        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card()
            self.ca_card_num = card_info[0]
            self.ca_card_pwd = card_info[1]
            self.cfg.set("env_para", "ca_card_num", self.ca_card_num)
            self.cfg.set("env_para", "ca_card_pwd", self.ca_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))
        
    #购买试听卡
    def test_buy_listen_card(self):
        ba = Base(self.driver)
        card_management.buy_listen_card(self.cfg, self.driver, self.base_url)
        payconfirm = u"付款成功！"
        
        time.sleep(4)
        payok = self.driver.execute_script("return $('.page-headline').text()").strip()
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(payconfirm, payok)
        
    #添加试听卡组
    def test_listen_cardgroup(self):
        ba = Base(self.driver)
        title = u"listen" + ba.rand_name()
        card_management.add_listen_cardgroup(self.cfg, self.driver, self.base_url, self.org_name, group_name=title)

        self.driver.implicitly_wait(10)
        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        #建卡,取考号密码
        if rs == True:
            card_info = self.add_and_get_card()
            self.l_card_num = card_info[0]
            self.l_card_pwd = card_info[1]
            self.cfg.set("env_para", "l_card_num", self.l_card_num)
            self.cfg.set("env_para", "l_card_pwd", self.l_card_pwd)
            self.cfg.write(open(self.cfg_file, "w"))
        

    def add_and_get_card(self, card_type=0):#添加卡并返回第一个卡号和密码
        ba = Base(self.driver)
        card_prifix = "c" + ba.rand_name()
        card_management.add_card(self.cfg, self.driver, self.base_url, self.org_name, card_prifix)
        if card_type == 0:
            time.sleep(3)
            self.driver.find_element_by_link_text(u"浏览卡").click()
            time.sleep(2)
            card_num = self.driver.execute_script("return $(\"input[name='groupCheck']:eq(0)\").parent().next().text()")
            time.sleep(2)
            card_pwd = self.driver.execute_script("return $(\".textaligncenter\:eq(4)\").text()")
            time.sleep(2) 
        else:
            time.sleep(3)                
            self.driver.find_element_by_css_selector("span.greenbtn35_text").click()
            time.sleep(2)
            card_num = self.driver.execute_script("return $(\"input[type='checkbox']:eq(1)\").parent().text()")
            time.sleep(2)
             #print 'card_num:',card_num
            card_pwd = self.driver.execute_script("return $(\"input[type='checkbox']:eq(1)\").parent().parent().next().children().text()") 
            time.sleep(2)
   
        return card_num, card_pwd


    #添加考试卡并返回第一个卡号
    def test_add_exam_card(self):
        ba = Base(self.driver)
        count = 5
        academy = "qqhru"
        self.examcard_num = card_management.add_exam_card(self.cfg, self.driver, self.base_url, count, academy)
        self.cfg.set("env_para", "examcard_num", self.examcard_num)
        self.cfg.write(open(self.cfg_file, "w"))
        if self.examcard_num == None:
           rs = False
        else:
           rs = True  
        filename = ba.save_screenshot()
        print "image:"+filename       
        self.assertEqual(True, rs)

    def tearDown(self): #在每个测试方法执行后调用，这个地方做所有清理工作
        self.driver.quit()