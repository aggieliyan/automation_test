# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time
from selenium import webdriver

import login
import new_course_management

def execute_func(func_name):
	func_name()
#课程类目
def course_cate():
	driver.find_element("id", "J_genTopCateg").click()#新建一级类目
	driver.refresh()

#课程管理
def course_manage():
	current_url = driver.current_url
	time.sleep(3)
	try:
		driver.find_element_by_link_text(u"获取视频链接").click()
		time.sleep(1)
	except:
		print u"没有课程读权限"

	try:		
		#编辑
		driver.get(current_url)
		driver.find_element_by_link_text(u"编辑").click()
		driver.execute_script("$('submit').click()")
		try:
			driver.find_element("id", "J_complete").click()
		except:
			pass
		time.sleep(1)
		#发布相似课程
		driver.get(current_url)
		time.sleep(2)
		driver.find_element_by_link_text(u"发布相似课程").click()
		time.sleep(1)
		#编辑三分屏章节
		driver.get(current_url)
		alert = driver.switch_to_alert()
		alert.accept()
		time.sleep(3)
		driver.find_element_by_link_text(u"编辑三分屏章节").click()
		time.sleep(1)
	except:
		print u"没有课程编辑权限"

	try:
		#删除
		driver.get(current_url)
		time.sleep(2)
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"没有课程删除权限"


def course():
	driver.get("%smyOffice.do" %(base_url))
	#course_func = [u'课程类目', u'课程管理', u'课件存储空间', u'视频外链管理', u'播放高级设置']
	course_func = {u"课程类目":course_cate, u"课程管理":course_manage,}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"教学教务").click()
		time.sleep(1)
		for item in course_func.keys():
			try:
				driver.implicitly_wait(5)
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
	base_url = "http://www.gamma.ablesky.com/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
	user_name = "sadm001"
	user_psw = "1234"

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
