# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time, random
from selenium import webdriver

import login
import new_course_management
import cate_management, student_management, new_course_management

def execute_func(func_name):
	func_name()

#教学互动-我的私信
def teaching_letter():
	time.sleep(1)
	try:
		driver.find_element_by_link_text(u"我的私信").click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的读权限"
		return
	time.sleep(2)	
	try:
		driver.find_element_by_class_name("sendEmialBtn").click()
		time.sleep(1)
		driver.find_element_by_name("username").send_keys("success")
		time.sleep(1)
		driver.find_element_by_name("subject").send_keys(u"标题")
		time.sleep(1)
		driver.find_element_by_name("msg").send_keys(u"内容")
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/div[10]/div[2]/div[2]/div/div/div/ \
			div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button").click()
	except Exception, e:
		print traceback.format_exc()
		print u"没有我的私信的编辑权限"
	time.sleep(3)		
	try:
		driver.find_element_by_class_name("deleteS").click()
		time.sleep(2)
		driver.find_elements_by_css_selector(".x-panel-btns-center .x-btn-center button")[1].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"发件箱").click()
		time.sleep(1)
		driver.find_element_by_css_selector(".priceAndFeedBGrid .deleteS").click()
		time.sleep(1)
		driver.find_elements_by_css_selector(".x-window-br .x-btn-text")[1].click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的删除权限"
				 
#教学互动-网校答疑    
def teaching_ansquestion():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"网校答疑").click()
	except Exception, e:
		print traceback.format_exc()
		print u"没有网校答疑的读权限"
		return	
	time.sleep(2)	   
	try:
	    driver.find_element_by_link_text(u"回复").click()#没有具体回复
	    time.sleep(1)
	    driver.find_element_by_link_text(u"取消").click() 
	    time.sleep(2)	
	    driver.find_element_by_link_text(u"编辑").click()
	    time.sleep(1)    
	    driver.find_element_by_link_text(u"保存").click() 	
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的编辑权限"  

	time.sleep(1)		 
	try:
	    driver.find_element_by_link_text(u"删除").click()
	except Exception, e:
		print traceback.format_exc()
		print u"没有我的私信的删除权限"  
		
#授权管理-授权购买记录	
def authmanage_buyRecord():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"授权购买记录").click()
	    time.sleep(1)
	    driver.find_element_by_class_name("cc-arrow").click()#下拉选择
	    time.sleep(1)
	    driver.find_elements_by_class_name("cc-item")[1].click()
	    time.sleep(2)	
	    driver.find_elements_by_class_name("j-gldp-target")[0].click()#日期筛选
	    time.sleep(1)    
	    driver.find_element_by_class_name("outday").click()
	    time.sleep(1)    
	    driver.find_elements_by_class_name("j-gldp-target")[1].click()
	    time.sleep(1)    
	    driver.find_elements_by_class_name("outday")[-1].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"查询").click()
	except Exception:
		print traceback.format_exc()
		print u"没有授权购买记录的读权限"
		return
		
	time.sleep(2)	   
	try:   
	    driver.find_element_by_link_text(u"购买授权").click()	    
	except Exception, e:
		print traceback.format_exc()
		print u"没有授权购买记录的编辑、删除权限"
		
#授权管理-已使用授权		
def authmanage_usegrant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"已使用授权").click()
	    time.sleep(1) 
	    driver.find_element_by_name("authType").click()#下拉选择扣除方式
	    time.sleep(1)
	    driver.find_elements_by_css_selector("select option")[1].click()
	    time.sleep(2)
	    driver.find_element_by_name("authStatus").click()#下拉选择状态
	    time.sleep(1)
	    driver.find_elements_by_css_selector("select option")[-1].click()
	    time.sleep(2)
	    driver.find_elements_by_class_name("x-form-date-trigger")[0].click()#日期筛选
	    time.sleep(1)
	    driver.find_element_by_class_name("x-date-active").click()
	    time.sleep(2)	
	    driver.find_elements_by_class_name("x-form-date-trigger")[1].click()
	    time.sleep(1)    
	    driver.find_elements_by_class_name("x-date-active")[-1].click()
	    time.sleep(2)
	    driver.find_element_by_class_name("x-btn-text").click()#点击过滤
	    time.sleep(1)	        
	except Exception:
		print traceback.format_exc()
		print u"没有已使用授权的读、编辑、删除权限"
		
#授权管理-在线购买授权	
def authmanage_buygrant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"在线购买授权").click()   
	except Exception:
		print traceback.format_exc()
		print u"没有在线购买授权的读权限"
		return
#	user_name = 'none'
#	bnum = 1
	current_url = driver.current_url
	time.sleep(1) 
	try:
	    driver.find_element_by_class_name("authorizeNum").clear()
	    time.sleep(1)
	    driver.find_element_by_class_name("authorizeNum").send_keys('1')
	    time.sleep(1)		
	    driver.find_element_by_link_text(u"确认购买").click()   
#		student_management.buy_open_num(cfg, driver, base_url, user_name, bnum)
	except Exception:
		print traceback.format_exc()
		print u"没有在线购买授权的编辑、删除权限"
	time.sleep(2)
	driver.get(current_url)

#课程合作代理-管理我授权的代理
def courseagent_grant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"管理我授权的代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_class_name("agency-navInfo").click()#接受or拒绝
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看课程").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看记录").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"订单管理").click()
 	    time.sleep(1)
 	    bh = driver.window_handles 	    
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(2)
 	    ah = driver.window_handles
 	    while len(bh) == len(ah):
		    ah = driver.window_handles
	    for h in ah:
		    if h not in bh:
			    driver.switch_to_window(h)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的读权限"
		return

	time.sleep(2) 
	try:
        #选择代理区域-手动测试
		driver.find_element_by_link_text(u"新建订单").click()  
		time.sleep(2)
		driver.get(current_url)
		time.sleep(2)
		#driver.find_elements_by_class_name("disMore_btn")[-1].click()
		#time.sleep(2)		
		#driver.find_elements_by_name("categoryItems")[-1].click()
		driver.find_element_by_link_text(u"订单管理").click()  
		time.sleep(1)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"修改订单").click()
		time.sleep(2)
		ah = driver.window_handles
		while len(bh) == len(ah):
		    ah = driver.window_handles
		for h in ah:
		    if h not in bh:
			    driver.switch_to_window(h)
		time.sleep(2)
#		driver.find_element_by_id("readProtocol").click()
#		time.sleep(1)
#		driver.find_element_by_link_text(u"发送订单").click()
#		time.sleep(1)
#		driver.find_element_by_link_text(u"确定").click()
		driver.get(current_url)
		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element_by_css_selector(".dialog-button-container button").click()
		time.sleep(1)
		driver.get(current_url)					  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的编辑权限、删除权限"######？？？？
	time.sleep(2)
	driver.get(current_url)
	
#课程合作代理-管理我申请的代理		
def courseagent_apply():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"管理我申请的代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_link_text(u"管理课程").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看记录").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"订单管理").click()
 	    time.sleep(1)
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(1)
 	    bh = driver.window_handles 	    
	    driver.find_element_by_link_text(u"订单详情").click()
 	    time.sleep(2)
 	    ah = driver.window_handles
 	    while len(bh) == len(ah):
		    ah = driver.window_handles
	    for h in ah:
		    if h not in bh:
			    driver.switch_to_window(h)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我申请的代理的读权限"
		return

	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	title = u"agencycourse"+rand_name 
	try:
        #管理课程
		new_course_management.release_agency_course(cfg, driver, base_url, course_title=title)
		driver.get(current_url)
		time.sleep(2)
		driver.find_element_by_link_text(u"订单管理").click()  
		time.sleep(1)
		driver.find_element_by_link_text(u"立即支付").click()
		ah = driver.window_handles
		while len(bh) == len(ah):
		    ah = driver.window_handles
		for h in ah:
		    if h not in bh:
			    driver.switch_to_window(h)
		time.sleep(2)
		driver.get(current_url)					  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的编辑权限、删除权限"######？？？？
	time.sleep(2)
	driver.get(current_url)

#教学互动		    
def teaching():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-我的私信、网校答疑
	teaching_func = {u"我的私信":teaching_letter, u"网校答疑":teaching_ansquestion,}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"后台首页").click()
		time.sleep(1)
		for item in teaching_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(teaching_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有教学互动-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有教学互动相关权限"
			
#授权管理
def authmanage():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-我的私信、网校答疑
	authmanage_func = {u"授权购买记录":authmanage_buyRecord, u"已使用授权":authmanage_usegrant,u"在线购买授权":authmanage_buygrant}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"后台首页").click()
		time.sleep(1)
		for item in authmanage_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(authmanage_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有授权管理-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有授权管理相关权限"      

#课程合作代理
def courseagent():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-我的私信、网校答疑
	authmanage_func = {u"管理我授权的代理":courseagent_grant, u"管理我申请的代理":courseagent_apply}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"后台首页").click()
		time.sleep(1)
		for item in authmanage_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(authmanage_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有授权管理-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有授课程合作代理相关权限"      

def admin_athority_check():
    
	global base_url
	global cfg 
	global driver
	base_url = "http://www.ablesky.com/"
#	base_url = "http://www.ablesky-a.com:8080/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
#	user_name = "v52"
#	user_psw = "1234"    
	user_name = "stu_gy"
	user_psw = "gy04110911"

	chromedriver = "C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
#	driver.get("%smyOffice.do" %(base_url))
	#teaching()
	#authmanage()
	courseagent()
	driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
