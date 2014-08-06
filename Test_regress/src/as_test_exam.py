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
        
        #考试系统部分
        as_test_regress.Test.login_from_index(self)
        self.exam_onequestion(self)
        self.exam_questions()
        self.import_questions()
        self.add_exam_subject()
        self.modify_exam_subject()
        self.delete_exam_subject()
        self.create_exam_cate()
        self.modify_exam_cate()
        self.delete_exam_cate() 
        self.add_exam_point()
        self.modify_exam_point()
        self.delete_exam_point()    
        self.createpaper()
        self.exam_student_management()
        self.user_statistical_information()
        login.logout(self.driver, self.base_url)
        
        self.login_user()
        self.exam_user()

                     

    def tearDown(self):
        self.driver.quit()
        fail_num = len(self.verificationErrors)
        print "total case:%s,%s failures.detail:%s"%(self.total,fail_num,self.verificationErrors)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()