# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time
from selenium import webdriver

import login

def execute_func(func_name):
	func_name()

def course_cate():
	driver.find_element("id", "J_genTopCateg").click()#新建一级类目
	driver.refresh()

def course_manage():
	try:
		driver.find_element_by_link_text(u"编辑").click()
		driver.execute_script("$('submit').click()")
		driver.get("%smyOffice.do" %(base_url))
		driver.find_element_by_link_text(u"教学教务").click()
		time.sleep(1)
	except:
		print u"没有课程编辑权限"


def course():
	driver.get("%smyOffice.do" %(base_url))
	#course_func = [u'课程类目', u'课程管理', u'课件存储空间', u'视频外链管理', u'播放高级设置']
	course_func = {u"课程类目":course_cate, u"课程管理":course_manage,}
	try:
		driver.implicitly_wait(10)
		driver.find_element_by_link_text(u"教学教务").click()
		time.sleep(5)
		for item in course_func.keys():
			try:
				driver.implicitly_wait(10)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(course_func[item])
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
	base_url = "http://www.ablesky.com/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
	user_name = ""
	user_psw = ""

	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
	course()

	driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
