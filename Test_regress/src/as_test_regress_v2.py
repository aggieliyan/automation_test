# -*- coding: UTF-8 -*-
'''
Created on Sep. 24, 2012

@author: yilulu
'''
import unittest, ConfigParser, random, time, os, logging, MySQLdb
import traceback

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner

import login, new_course_management, course_management, student_management, \
card_management, cate_management, admin_management, user_management, exam_paper, exam_questions, exam_cate_management
import exam_user_management

from selenium.webdriver.common.by import By
import HTMLTestRunner

import PO.org_card_page, PO.org_cate_page, PO.org_student_page

from PO.base import Base
from PO.org_cate_exam import OrgExamCreateListPage, OrgExamInputListPage, OrgExamiOkListPage, OrgExamSearchListPage
from testcase_student import StudentTest

class Test(unittest.TestCase):
    

    def setUp(self):
        self.verificationErrors = []
        self.browser = "Chrome"
        self.cfg_file = 'config.ini'
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(self.cfg_file)
        self.verificationErrors = []
        self.org_name = self.cfg.get("env_para", "org_name")
        self.org_password = self.cfg.get("env_para", "org_password")
        self.user_name = self.cfg.get("env_para", "user_name")
        self.user_password = self.cfg.get("env_para", "user_password")
        self.base_url = self.cfg.get("env_para", "base_url")

        self.total = 0


        #一些使用卡相关变量，前置条件：管理员先创建卡，给变量赋值，用户才可获取卡号登录使用卡号
        #充值卡-卡号、密码
        self.p_card_num = 0
        self.p_card_pwd = 0
        #充课卡-卡号、密码
        self.c_card_num = 0
        self.c_card_pwd = 0
        #补课卡-卡号、密码
        self.ca_card_num = 0
        self.ca_card_pwd = 0
        #试听卡-考号、密码
        self.l_card_num = 0
        self.l_card_pwd = 0
        #考试卡-卡号
        self.examcard_num = 0

        #注册的时候会把第一个值赋给它
        self.import_name = ""

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
 
    @unittest.skip("test")
    def test_release_normal_course(self):      
        ba = Base(self.driver)
        title = "course" + ba.rand_name()
        new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title, course_price=10)
        
        rs = ba.is_element_present("link text", u"查看课程")
        self.assertEqual(True, rs)
        ba.save_screenshot()
     

        # self.normal_course = title#待用-在数据库中查是否转换失败

          
        #取链接待后面购买
        # course_href = self.driver.execute_script("return $(\"a:contains(\'"+title+"\')\").attr('href')")
        # time.sleep(1)
        # if course_href:
        #     self.course_href = self.base_url + course_href
        # else:
        #     self.course_href = ""

    @unittest.skip("test")
    def test_release_three_video(self):
        ba = Base(self.driver)
        title = "coursethree" + ba.rand_name()
        new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title)
        
        rs = ba.is_element_present("link text", u"查看课程")
        self.assertEqual(True, rs)
        ba.save_screenshot()

    @unittest.skip("test")
    def test_release_two_video(self):
        ba = Base(self.driver)
        title = "two_video" + ba.rand_name()
        new_course_management.course_redirect(self.cfg, self.driver, self.base_url, course_title=title, course_price=10)
        
        rs = ba.is_element_present("link text", u"查看课程")
        self.assertEqual(True, rs)
        ba.save_screenshot()

    @unittest.skip("test")
    def test_presaleclass(self):
        ba = Base(self.driver)
        title = "presaleclass" + ba.rand_name()
        new_course_management.class_redirect(self.cfg, self.driver, self.base_url, ctype=2, classname=title)

        course = self.driver.find_element("link text", title)
        #若发课成功了取出课程链接存入文件中供后面的购买流程用
        rs = False
        if course:
            rs = True
            self.cfg.set("env_para", "course_href1", course.get_attribute("href"))
            self.cfg.write(open(self.cfg_file, "w"))
        
        filename = ba.save_screenshot()
        print "image:"+filename

        self.assertEqual(True, rs)

    @unittest.skip("test")
    def test_onlineclass(self):
        ba = Base(self.driver)
        title = "onlineclass" + ba.rand_name()
        new_course_management.class_redirect(self.cfg, self.driver, self.base_url, classname=title)

        # rs = ba.is_element_present("link text", title)
        course = self.driver.find_element("link text", title)
        #若发课成功了取出课程链接存入文件中供后面的购买流程用
        rs = False
        if course:
            rs = True
            self.cfg.set("env_para", "course_href2", course.get_attribute("href"))
            self.cfg.write(open(self.cfg_file, "w"))

        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)
        


    @unittest.skip("test")
    def test_agency_course(self):
        ba = Base(self.driver)
        title = "agency" + ba.rand_name()
        new_course_management.release_agency_course(self.cfg, self.driver, self.base_url, course_title=title)

        rs = ba.is_element_present("link text", title)
        filename = ba.save_screenshot()
        print "image:"+filename
        self.assertEqual(True, rs)

    @unittest.skip("test")
    def test_create_admin(self):
        aname = admin_management.auto_create_admin(self.cfg, self.driver, adm_num=1)
        lastadmin = self.driver.execute_script("return $('.floatleft').eq(-10).text()")

        self.assertEqual(aname, lastadmin)

    @unittest.skip("test")    
    def test_register(self):
        ba = Base(self.driver)
        user_name = ""
        user_name = login.auto_register(self.cfg, self.driver, self.base_url, 1, 1)
        self.import_name = user_name
        
        filename = ba.save_screenshot()
        print "image:"+filename

    def test_release_announcement(self):
        ba = Base(self.driver)

        title = ba.rand_name()
        user_management.release_announcement(self.cfg, self.driver, self.base_url, self.org_name, title)
        
    def tearDown(self): #在每个测试方法执行后调用，这个地方做所有清理工作
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)
        # fail_num = len(self.verificationErrors)
        # print "total case:%s, %s failures.detail:%s"%(self.total, fail_num, self.verificationErrors)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    # unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    # testsuite = unittest.TestSuite()
    # testsuite.addTest(Test("test_release_normal_course"))
    # testsuite.addTest(Test("test_create_admin"))
    # testsuite = unittest.TestLoader().loadTestsFromTestCase(Test)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test)
#    suite2 = unittest.TestLoader().loadTestsFromTestCase(ttStudentTest)
    allsuites = [suite1]
    alltests = unittest.TestSuite(allsuites)


    #file_name = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time())) + '.html'
    fp = file("myreport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    runner.run(alltests)

    cfg_file = 'config.ini'
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfg_file)
    cfg.set("env_para", "cookie1", "no")
    cfg.set("env_para", "cookie_stu", "no")
    cfg.write(open(cfg_file, "w"))
