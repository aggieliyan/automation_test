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
#课程类目
def course_cate():
	current_url = driver.current_url
	#修改
	try:
		#新建一级类目
	    cate_management.add_cate(cfg, driver, base_url)
        
        #隐藏类目操作
	    #driver.find_element("class name", "trueFrame").click()
	    #driver.execute_script("$('.trueFrame').eq(0).click()")
	    #time.sleep(1)

	    #添加课程到类目中
	    cate_management.add_courese_to_cate(cfg, driver, base_url)
	    driver.get(current_url)

	    #添加子类目
	    driver.find_element("class name", "addSub").click()
	    time.sleep(1)
	    driver.find_element("id", "reg_textField").clear()
	    driver.find_element("id", "reg_textField").send_keys("sub_cate")
	    time.sleep(1)
	    driver.find_element("xpath", "//button").click()

	except:
		print traceback.format_exc()
		print u"没有类目的编辑权限"


	try:
	    #删除类目
	    cate_management.delete_cate(cfg, driver, base_url)
	except:
		print traceback.format_exc()
		print u"没有类目删除权限"

#课程管理
def course_manage():
	#取当前页面的链接，后面的操作后能回来
	current_url = driver.current_url
	time.sleep(3)
	try:
		driver.find_element_by_link_text(u"获取视频链接").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
	except:
		print traceback.format_exc() 
		print u"没有课程读权限"

	try:		
		#编辑
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

		#发布课程
		driver.get(current_url)
		driver.find_element("class name", "new-categ-button")
		new_course_management.course_redirect(cfg, driver, base_url)
	except:
		print traceback.format_exc() 
		print u"没有课程编辑权限"

	try:
		#删除
		driver.get(current_url)
		time.sleep(2)
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)

		
		#批量删除-手测
		# driver.find_element("id", "J_selAll").click()
		# driver.find_elements("class name", ".cc-textbox")[-1].click()
		# driver.find_element("class name", ".cc-item").click()
		# time.sleep(1)
		# driver.find_element("xpath", "//button").click()

	except:
		print traceback.format_exc()
		print u"没有课程删除权限"

#课件存储空间
def course_space():
	pass

#课程外链管理
def course_href():   
    #读权限
    try:
    	driver.find_element("id", "J_exportCourseLinks").click()
    	time.sleep(1)
    except:
		print u"不能导出课程链接"
    
    #修改权限
    try:
		driver.find_element_by_link_text("添加绑定域名").click()
		time.sleep(1)
		driver.find_element("id", "handleWebInput").send_keys("www.baidu.com")
		driver.find_elements("xpath", "//button")[-2].click()
        
		time.sleep(1)
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-2].click()
    except:
		print traceback.format_exc()
		print u"没有外链编辑权限"
    #删除
    try:
    	driver.find_element_by_link_text(u"删除").click()
        time.sleep(1)
        driver.find_elements("xpath", "//button")[-2].click()
    except:
		print u"没有外链删除权限"
def course_setting():
	try:
		driver.find_element("id", "editCourseWare").click()
		time.sleep(1)
		driver.find_elements("class name", "bluebtn25_text")[-1].click()
		time.sleep(1)
	except:
		print u"没有高级设置编辑权限"

def course():
	driver.get("%smyOffice.do" %(base_url))
	course_func = {u"课程类目":course_cate, 
	               u"课程管理":course_manage, 
	               u"课件存储空间":course_space, 
	               u'视频外链管理':course_href,
	               u'播放高级设置':course_setting,}
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

def class_manage():
	current_url = driver.current_url

	try:
		#编辑
		driver.find_element_by_link_text("编辑").click()
		time.sleep(1)
		driver.find_element("css selector", "span.greenbtn25_text").click()

		#下架
		time.sleep(1)
		driver.find_element_by_link_text("下架").click()

		#报名详情
		driver.find_element_by_link_text("报名详情").click()
		time.sleep(1)
		driver.find_element("css selector", "span.greenbtn25_text").click()
		time.sleep(1)
	except:
		print u"没有报班管理-编辑权限"

	try:
		#删除
		driver.get(current_url)
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"没有报班管理-删除权限"


def class_center():
	driver.get("%smyOffice.do" %(base_url))
	course_func = {u"报班管理":class_manage,}
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
	user_name = "salesdemo"
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
