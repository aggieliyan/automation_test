# -*- coding: UTF-8 -*-
import unittest, ConfigParser, random, time, os
import traceback

from selenium import webdriver

import login
import exam_paper
from PO.base import Base

class ExamResultTest(unittest.TestCase):

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
        self.paper_name = self.cfg.get("env_para", "paper_name")
        self.dbhost = self.cfg.get("env_para", "dbhost")

        if os.path.exists("C:\\test_rs_pic") != True:
                os.system("mkdir C:\\test_rs_pic")

        if self.browser == 'ie':
            self.driver = webdriver.Ie()
        elif self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'Chrome':
            # chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
            # os.environ["webdriver.chrome.driver"] = chromedriver
            # self.driver = webdriver.Chrome(chromedriver)
            self.driver = webdriver.Chrome()
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

   #为学员评分
    # @unittest.skip("test")        
    def test_score_paper(self):
        ba = Base(self.driver)
        score = 0   
        score = exam_paper.exam_result(self.cfg, self.driver, self.base_url, exam_name=self.paper_name, etype=3, username=self.user_name)        

        #验证
        ascore = self.driver.execute_script("$(\"a:contains('"+self.user_name+"')\").parents('.odd').children().eq(4).text()")
        self.assertEqual(score, ascore)
        filename = ba.save_screenshot()
        print "image:"+filename
    # @unittest.skip("test")
    #导出开放试卷的结果
    def test_export_openpaper_result(self):
        ba = Base(self.driver)      
        paper_name = self.cfg.get("env_para", "paper_name")
        exam_paper.exam_result(self.cfg, self.driver, self.base_url, exam_name=self.paper_name, etype=2, username=self.user_name)        
        filename = ba.save_screenshot()
        print "image:"+filename

    # @unittest.skip("test")
    #导出分发试卷的结果
    def test_export_sendpaper_result(self):
        ba = Base(self.driver)
        paper_name = self.cfg.get("env_para", "paper_name")
        exam_paper.exam_result(self.cfg, self.driver, self.base_url, exam_name=self.paper_name, etype=1, username=self.user_name)        
        filename = ba.save_screenshot()
        print "image:"+filename

    def tearDown(self):
        self.driver.quit()