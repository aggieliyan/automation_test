# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time
from selenium import webdriver

import login
import new_course_management
import cate_management

def execute_func(func_name):
	func_name()

#教学互动-我的私信
def teaching_letter():
	driver.find_element_by_link_text(u"我的私信").click()
#教学互动-网校答疑    
#def teaching_ansquestion():

def fir():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-我的私信、网校答疑
	teaching_func = {u"我的私信":teaching_letter, u"网校答疑":teaching_ansquestion,}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"教学教务").click()
		time.sleep(1)
		for item in teaching_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(teaching_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有教务管理-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有教学教务相关权限"
		return



def admin_athority_check():
    
	global base_url
	global cfg 
	global driver
	base_url = "http://www.beta.ablesky.com/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
	user_name = "stu_gy01"
	user_psw = "gy0411"

	chromedriver = "C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)


	driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
