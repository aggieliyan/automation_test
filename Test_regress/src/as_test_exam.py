# -*- coding: UTF-8 -*-
'''
Created on Jul 30, 2014

@author: liwen
'''
import unittest,ConfigParser,random,time,os,MySQLdb
from selenium import webdriver
import login, new_course_management, course_management, student_management, card_management,cate_management,admin_management,user_management,exam_paper, exam_questions,exam_cate_management,as_test_regress
import exam_user_management
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):


    def setUp(self):
        
        self.browser = "firefox"
        self.test_enviroment = "beta"  
        self.org_name = "salesdemo"
        self.org_password = "1234"
        self.user_name = "yilu282"
        self.user_password = "1234"
        self.dbhost = "192.168.120.201" #alpha数据库地址：192.168.150.7、beta: 192.168.120.201 omega数据库：192.168.190.74 beta数据库192.168.3.50 gamma: 192.168.120.110r
        #self.independent_url = "www.dlym.com"#独立域名网址
        self.import_name = "sun122"
        
        cfg_file = 'config.ini'
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(cfg_file)
        self.verificationErrors = []
        
        self.total = 0
        
        if self.browser == 'ie':      
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            self.driver =  webdriver.Chrome(chromedriver)
        elif self.browser == "Html":
            self.driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        else:
            self.driver = webdriver.Ie()

        self.driver.implicitly_wait(5)
        self.base_url = "http://www."+self.test_enviroment+".ablesky.com/"
        #self.base_url = "http://www.zhongyan.com/"
        
        if os.path.exists("C:\\test_rs_pic")!= True:
            os.system("mkdir C:\\test_rs_pic")
    
    def connect_db(self,database):
        try:
            conn = MySQLdb.connect(host=self.dbhost, user='root',passwd='mysqlpwd1',db=database,charset='utf8')
        except Exception,e:
            print e
        return conn
    
    def test_regress(self):
        
        #网站主站回归流程
        #self.register()
        login.login_by_as(self.cfg, self.driver, self.base_url, self.org_name, self.org_password)
        

        #考试系统部分
        #as_test_regress.use_exam_card() 
        #as_test_regress.import_questions()
        #as_test_regress.add_exam_subject()
        #as_test_regress.modify_exam_subject()
        #as_test_regress.delete_exam_subject()
        #as_test_regress.create_exam_cate()
        #as_test_regress.modify_exam_cate()
        #as_test_regress.delete_exam_cate() 
        #as_test_regress.add_exam_point()
        #as_test_regress.modify_exam_point()
        #as_test_regress.delete_exam_point()  
        #as_test_regress.exam_questions()
        exam_paper.auto_createpaper(self.cfg,self.driver,self.base_url,0, 0, 0, 1)
        #exam_paper.send_close_paper(self.cfg, self.driver, self.base_url, atype=1)
        #exam_paper.send_close_paper(self.cfg, self.driver, self.base_url, atype=2)
        #exam_paper.exam_result(self.cfg, self.driver, self.base_url, exam_name=u"未作答（主观题，免费）", etype=1)
        #exam_paper.exam_result(self.cfg, self.driver, self.base_url, exam_name=u"未作答（主观题，免费）", etype=2)
        #exam_paper.exam_result(self.cfg, self.driver, self.base_url, exam_name=u"未作答（主观题，免费）", etype=3)
        #login.logout(self.driver, self.base_url)

        #as_test_regress.login_user()
        #self.use_prepaidcard()
        #self.use_coursecard()
        #self.use_catecard()
        #self.use_listencard()
        #self.use_exam_card()          
        #self.release_announcement()
        #self.modify_pagefoot()  
        #self.change_headpic()
        #self.change_homelogo()
        #self.wailian_video()          
        #self.buy_course_use_RMB()
        #self.buy_course_use_card()        
        #self.manage_course_num()
        
        #学员考试
        #exam_user_management.buy_paper(self.cfg, self.driver, self.base_url)
        #self.exam_user()

                     

    def tearDown(self):
        self.driver.quit()
        fail_num = len(self.verificationErrors)
        print "total case:%s,%s failures.detail:%s"%(self.total,fail_num,self.verificationErrors)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()