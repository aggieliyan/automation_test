# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time, random
from selenium import webdriver

import login
import new_course_management
import cate_management, student_management, new_course_management, card_management

def execute_func(func_name):
	func_name()

def check_menu(menu_title, menu_dic):
	try:
		time.sleep(2)
		ahref = driver.find_element_by_link_text(menu_title).get_attribute("href")
		#print ahref
		if ahref == "javascript:;":
			print u"没有%s权限"%menu_title
			return
		else:
			driver.find_element_by_link_text(menu_title).click()
		time.sleep(1)
		for item in menu_dic.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(menu_dic[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有%s-%s权限"%(menu_title, item)
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有%s权限"%menu_title

#切换窗口公共方法
def swithing_window(bh,ah):
	 while len(bh) == len(ah):
	     ah = driver.window_handles
	 for h in ah:
	     if h not in bh:
		     driver.switch_to_window(h)	
		     	
#后台首页-教学互动		    
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
			
#后台首页-授权管理
def authmanage():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-授权购买记录、已使用授权 在线购买授权
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

#后台首页-课程合作代理
def courseagent():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-管理我授权的代理、管理我申请的代理
	authmanage_func = {u"管理我授权的代理":agent_grant, u"管理我申请的代理":agent_apply}
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
		
#后台首页-学习卡
def learnigcard():
	driver.get("%smyOffice.do" %(base_url))
	#学习卡-管理卡组、卡使用记录
	learnigcard_func = {u"管理卡组":learnigcard_group, u"卡使用记录":learnigcard_record}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"后台首页").click()
		time.sleep(1)
		for item in learnigcard_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(learnigcard_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有学习卡-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有学习卡相关权限"

#后台首页-统计管理
def countmanage():
	driver.get("%smyOffice.do" %(base_url))
	#统计管理-外链视频流量统计  浏览量统计 新增学员量统计
	countmanage_func = {u"外链视频流量统计":countmanage_outvideo, u"浏览量统计":countmanage_views, u"新增学员量统计":countmanage_newstudent}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"后台首页").click()
		time.sleep(1)
		for item in countmanage_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				time.sleep(1)
				execute_func(countmanage_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有统计管理-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有统计管理相关权限"     
		
		      

#系统设置-------------
      
        
#学员/员工-网校学员
def stuoremp():
	driver.get("%smyOffice.do" %(base_url))
	#统计管理-外链视频流量统计  浏览量统计 新增学员量统计
	stuoremp_func = {u"学员类目":stuoremp_stucate, u"学员管理":stuoremp_stumanage, \
	    u"员工管理":stuoremp_empmanage, u"员工申请 ":stuoremp_empapply, u"学员学习记录":stuoremp_stulearnrecord}
	try:
		time.sleep(2)
		driver.find_element_by_link_text(u"学员/员工").click()
		time.sleep(1)
		for item in stuoremp_func.keys():
			try:
				driver.implicitly_wait(5)
				driver.find_element_by_link_text(item).click()
				execute_func(stuoremp_func[item])
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有网校学员-%s权限"%item
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有网校学员相关权限"   
		
#教学互动-我的私信
def teaching_letter():
	time.sleep(1)
	try:
		driver.find_element_by_class_name("x-tab-strip-text").click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的读权限"
		return
	time.sleep(2)	
	try:
		driver.find_element_by_class_name("sendEmialBtn").click()#发送私信
		time.sleep(1)
		driver.find_element_by_name("username").send_keys("success")
		time.sleep(1)
		driver.find_element_by_name("subject").send_keys(u"标题")
		time.sleep(1)
		driver.find_element_by_name("msg").send_keys(u"内容")
		time.sleep(1)
		driver.find_element_by_css_selector(".x-panel-btn-td button").click()
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
		driver.find_element_by_class_name("x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements_by_class_name("x-combo-list-item")[0].click()
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
	current_url = driver.current_url
	time.sleep(2)
	try:
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
 	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的读权限"
		return

	time.sleep(2) 
	try:
		driver.find_element_by_class_name("agency-province").click()#选择代理区域
		time.sleep(1)
		driver.find_elements_by_css_selector(".agency-province option")[2].click()
		time.sleep(1)
		driver.find_element_by_class_name("agency-city").click()#选择代理区域
		time.sleep(1)
		driver.find_elements_by_css_selector(".agency-city option")[2].click()
		time.sleep(1)
		driver.find_element_by_class_name("agency-rank").click()#选择代理级别
		time.sleep(1)
		driver.find_elements_by_css_selector(".agency-rank option")[2].click()
		time.sleep(1)    
		driver.find_element_by_link_text(u"新建订单").click()#新建订单  
		time.sleep(3)		
		driver.find_elements_by_name("categoryItems")[-1].click()
		time.sleep(2)
		driver.find_element_by_id("J_acceptProtocol").click()
		time.sleep(2)
		driver.find_element_by_class_name("x-btn-text").click()
		time.sleep(2)
		driver.find_element_by_css_selector(".dialog-button-container button").click()#点击确定
		time.sleep(2)		
#		driver.get(current_url)
#		time.sleep(2)
#		driver.find_element_by_link_text(u"订单管理").click()  
#		time.sleep(1)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"修改订单").click()#进行修改订单
		time.sleep(2)
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(2)
		driver.find_element_by_id("J_acceptProtocol").click()
		time.sleep(1)
		driver.find_element_by_class_name("x-btn-text").click()
		time.sleep(1)
		driver.find_element_by_css_selector(".dialog-button-container button").click()
#		driver.get(current_url)
#		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element_by_css_selector(".dialog-button-container button").click()
		time.sleep(1)				  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限、删除权限"######？？？？
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
	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我申请的代理的课程代理的读权限"
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
		try:
		    driver.find_element_by_link_text(u"立即支付").click()
		    ah = driver.window_handles
		    swithing_window(bh,ah)
		    time.sleep(1)
		except:
			print "没有立即支付的课程订单"
		driver.get(current_url)					  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限、删除权限"######？？？？
	time.sleep(2)
	
#管理我授权的代理-考试代理
def paperagent_grant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"考试代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_link_text(u"查看试卷").click()
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
	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的考试代理的读权限"
		return

	time.sleep(2) 
	try:
		driver.find_element_by_class_name("agency-province").click()#选择代理区域
		time.sleep(1)
		driver.find_elements_by_css_selector(".agency-province option")[2].click()
		time.sleep(1)
		driver.find_element_by_class_name("agency-city").click()#选择代理区域
		time.sleep(1)
		driver.find_elements_by_css_selector(".agency-city option")[2].click()
		time.sleep(1)
		driver.find_element_by_class_name("agency-rank").click()#选择代理级别
		time.sleep(1)
		driver.find_elements_by_css_selector(".agency-rank option")[2].click()
		time.sleep(1)    
		driver.find_element_by_link_text(u"新建订单").click()#新建订单 
		time.sleep(2)  
		driver.find_element_by_link_text(u"全选试卷").click()
		time.sleep(2)
		driver.find_element_by_id("readed_check").click()
		time.sleep(2)
		driver.find_element_by_id("submit_btn").click()
		time.sleep(2)
		driver.find_element_by_css_selector(".dialog-button-container button").click()#点击确定
		time.sleep(2)		
#		driver.get(current_url)
#		time.sleep(2)
#		driver.find_element_by_link_text(u"订单管理").click()  
#		time.sleep(1)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"修改订单").click()#进行修改订单
		time.sleep(2)
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(2)
		driver.find_element_by_id("readed_check").click()
		time.sleep(1)
		driver.find_element_by_id("submit_btn").click()
		time.sleep(1)
		driver.find_element_by_css_selector(".dialog-button-container button").click()
#		driver.get(current_url)
#		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element_by_css_selector(".dialog-button-container button").click()
		time.sleep(1)			  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的考试代理的编辑权限、删除权限"
	driver.get(current_url)	
	time.sleep(2)
#管理我申请的代理-考试代理
def paperagent_apply():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"考试代理").click()
	    current_url = driver.current_url
	    time.sleep(2)
	    driver.find_element_by_link_text(u"管理试卷").click()
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
	    swithing_window(bh,ah)
 	    time.sleep(1)	     	    
	    driver.get(current_url)     
	except Exception:
		print traceback.format_exc()
		print u"没有管理我申请的代理的考试代理的读权限"
		return

	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	title = u"agencycourse"+rand_name 
	try:
        #管理试卷
	    driver.find_element_by_link_text(u"管理试卷").click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"编辑").click()#编辑试卷
	    ah = driver.window_handles
	    swithing_window(bh,ah)
	    time.sleep(1)
	    driver.find_element_by_id("paper_name_input").clear()
	    time.sleep(1)
	    driver.find_element_by_id("paper_name_input").send_keys(title)
	    time.sleep(1)
	    driver.find_element_by_id("save_btn").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1) 	    
	    driver.find_element_by_link_text(u"订单管理").click()
 	    bh = driver.window_handles  
	    time.sleep(1)
	    try:  
	        driver.find_element_by_link_text(u"立即支付").click()
	        ah = driver.window_handles
	        swithing_window(bh,ah)
	        time.sleep(1)
	    except:
	    	print "没有立即支付的考试订单"				  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限、删除权限"
	driver.get(current_url)	
	time.sleep(2)
	
#管理我授权的代理	
def agent_grant():
	courseagent_grant()
	paperagent_grant()

#管理我申请的代理	
def agent_apply():
	courseagent_apply()
	paperagent_apply()

#学习卡-管理卡组
def learnigcard_group():
	time.sleep(1)
	current_url = driver.current_url	
	try:
	    driver.find_element_by_link_text(u"浏览卡").click()
	    time.sleep(1)
	    driver.get(current_url)	
	except Exception:
		print traceback.format_exc()
		print u"没有管理卡组的读权限"
		return
		
	time.sleep(2)	   
	try: 
	    driver.find_element_by_link_text(u"购买试听卡").click()
		#card_management.buy_listen_card(cfg,driver,base_url)#购买试听卡
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
	    org_name = "stu_gy"
	    rand_name = str(random.randint(1000, 9999))
	    group_name = u"prepaidcard"+rand_name
	    group_price = 100
	    card_management.add_prepaid_cardgroup(cfg, driver, base_url, org_name, group_name, group_price)#添加卡组
	    card_prifix = "auto" + chr(random.randint(97, 122)) + \
		chr(random.randint(97, 122)) + chr(random.randint(97, 122))
	    card_management.add_card(cfg, driver, base_url, org_name,card_prifix)#添加卡
		#driver.find_element_by_link_text(u"添加卡组").click()	
		#time.sleep(1)
		#driver.get(current_url)
		#time.sleep(1)
		#driver.find_element_by_link_text(u"添加卡").click()	
		#time.sleep(1)
		#driver.get(current_url)
	    time.sleep(1)
	    driver.find_element_by_link_text(u"浏览卡").click()		
	    time.sleep(1)
	    driver.find_elements_by_css_selector("input[type=checkbox]")[1].click()#勾选第一个卡
	    time.sleep(1)
	    driver.find_element_by_class_name("x-form-arrow-trigger").click()#禁用
	    time.sleep(1)
	    driver.find_elements_by_class_name("x-combo-list-item")[1].click()
	    time.sleep(1)
	    driver.find_element_by_link_text("应用").click()#应用
	    time.sleep(2)
	    driver.find_elements_by_css_selector("input[type=checkbox]")[1].click()#勾选第一卡
	    time.sleep(1)
	    driver.find_element_by_class_name("x-form-arrow-trigger").click()#启用
	    time.sleep(1)	    
	    driver.find_elements_by_class_name("x-combo-list-item")[2].click()
	    time.sleep(1)
	    driver.find_element_by_link_text("应用").click()#应用
	    time.sleep(1)
	    driver.find_elements_by_class_name("colorwhite")[1].click()#点击向该卡组添加卡
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)	    
	    driver.find_element_by_link_text(u"编辑卡组").click()#编辑卡组
	    time.sleep(1)
	    driver.find_element_by_class_name("x-btn-text").click()#保存修改
	    time.sleep(1)					  
	except Exception, e:
		print traceback.format_exc()
		print u"没有管理卡组的编辑权限"
		
	time.sleep(2)	   
	try:
	    driver.find_element_by_link_text(u"浏览卡").click()		
	    time.sleep(1)
	    driver.find_elements_by_css_selector("input[type=checkbox]")[1].click()#勾选第一个卡
	    time.sleep(1)
	    driver.find_element_by_class_name("x-form-arrow-trigger").click()#删除
	    time.sleep(1)
	    driver.find_elements_by_class_name("x-combo-list-item")[0].click()
	    time.sleep(1)
	    driver.find_element_by_link_text("应用").click()#应用
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
	    driver.find_element_by_link_text(u"删除卡组").click()
	    time.sleep(1)
	    driver.find_elements_by_css_selector(".x-panel-bwrap .x-btn-text")[5].click()
	    time.sleep(1)
	except Exception, e:
		print traceback.format_exc()
		print u"没有管理卡组的删除权限"
#学习卡-卡使用记录	
def learnigcard_record():
	time.sleep(1)
	try:
	    driver.find_element_by_class_name("x-form-arrow-trigger").click()#下拉选择充卡类型
	    time.sleep(2)
	    driver.find_elements_by_class_name("x-combo-list-item")[-1].click()
	    time.sleep(1)
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
		print u"没有卡使用记录的读、编辑、删除权限"

#统计管理-外链视频流量统计
def countmanage_outvideo():
	time.sleep(1)
	try:
	    driver.find_element_by_css_selector("div[data-type=cur-year]").click()#点击本年
	    time.sleep(1)
	    driver.find_element_by_class_name("x-form-arrow-trigger").click()#按日显示
	    time.sleep(2)	
	    driver.find_elements_by_class_name("x-combo-list-item")[0].click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有外链视频流量统计的读、编辑、删除权限"
		
#统计管理-浏览量统计
def countmanage_views():
	time.sleep(1)
	try:
	    driver.find_element_by_css_selector("span[data-type=recent3month]").click()#点击最近3个月
	    time.sleep(1)
	    driver.find_element_by_class_name("cc-arrow").click()#按日查询
	    time.sleep(2)	
	    driver.find_elements_by_class_name("cc-item")[0].click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有浏览量的读、编辑、删除权限"
		
#统计管理-新增学员量统计	
def countmanage_newstudent():
	time.sleep(1)
	try:
	    driver.find_element_by_css_selector("span[data-type=last-month]").click()#点击上个月
	    time.sleep(1)
	    driver.find_element_by_class_name("cc-arrow").click()#按日查询
	    time.sleep(2)	
	    driver.find_elements_by_class_name("cc-item")[0].click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有新增学员量统计的读、编辑、删除权限"		


   
#系统设置-----------------
   
   

#网校学员-学员类目   
def stuoremp_stucate():
	time.sleep(1)
	current_url = driver.current_url
	try:
		driver.find_element_by_class_name("expandSub ")#找到展开图标
		time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员类目的读权限"

	time.sleep(1)
	try:
	    driver.find_element_by_id("J_genTopCateg").click()#新建一级类目
	    creat_stucate()#新建一级类目
	    driver.get(current_url)
	    bh = driver.window_handles
	    manage_catestu(bh)#管理类目学员
	    bh = driver.window_handles 
	    opencourseBatch(bh)#批量开通课程
	    driver.get(current_url)
	    driver.find_element_by_class_name("editCateg").click()#编辑类目
	    time.sleep(1)
	    driver.find_element_by_class_name("x-btn-text").click()#点击确定		
	    time.sleep(1)
	    driver.find_element_by_class_name("addSub").click()#添加子类目
	    creat_stucate()
	    time.sleep(1)				    
	except Exception:
		print traceback.format_exc()
		print u"没有学员类目的编辑权限"

	time.sleep(2)
	try:
	    driver.find_elements_by_class_name("delete")[-1].click()#删除类目
	    time.sleep(1)
	    driver.find_element_by_class_name("x-btn-text").click()#点击删除		
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员类目的删除权限"
						
#新建一级类目和子类目的方法		
def creat_stucate():
	time.sleep(1)
	rand_name = str(random.randint(1000, 9999))
	cate_name = u"catetest" + rand_name
	try:
	   driver.find_element_by_id("reg_topCateName").send_keys(cate_name)#输入类目名称
	except:
		None
	try:
	   driver.find_element_by_id("reg_textField").send_keys(cate_name)#输入类目名称
	except:
		None		
	time.sleep(1)
	driver.find_element_by_class_name("x-btn-text").click()#点击确定			
	time.sleep(1)

#管理类目学员的方法
def manage_catestu(bh):
	time.sleep(3)
	driver.find_element_by_class_name("manageCategStudent").click()
	ah = driver.window_handles
	swithing_window(bh,ah)
	time.sleep(3)
	driver.find_element_by_link_text(u"添加现有学员").click()
	time.sleep(2)
	driver.find_element_by_link_text(u"全部").click()
	time.sleep(2)
	driver.find_elements_by_css_selector(".x-panel-bwrap .x-btn-text")[-1].click()
	time.sleep(2)
	driver.find_element_by_link_text(u"返回").click()
	time.sleep(2)

#批量开通课程
def opencourseBatch(bh):
	time.sleep(1)
	driver.find_elements_by_class_name("openCourseBatch")[0].click()
	time.sleep(3)
	ah = driver.window_handles
	swithing_window(bh,ah)
	driver.find_elements_by_css_selector("input[type=checkbox]")[-1].click()#勾选最后一个课程类目
	time.sleep(2)
	driver.find_element_by_class_name("x-btn-text").click()
	time.sleep(2)
	driver.find_elements_by_css_selector(".x-btn-center .x-btn-text")[1].click()
	time.sleep(3)		
#网校学员-学员管理
def stuoremp_stumanage():
	time.sleep(2)
	current_url = driver.current_url
	try:
	    driver.find_element_by_link_text(u"筛选").click()#点击筛选
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的读权限"
		return
	
	org_name = "stu_gy"
	user_name = "stu_gy50"
	stu_num = 5
	time.sleep(1)
	try:
		driver.find_element_by_link_text(u"批量导入学员").click()#批量导入学员
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"批量创建学员").click()#批量创建学员
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"开通课程").click()#开通课程
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
		driver.find_element_by_link_text(u"管理播放授权数").click()#管理播放授权数
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
		driver.find_element_by_link_text(u"延长授权").click()#延长授权
		time.sleep(1)
		driver.find_elements_by_class_name("x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作手动测试 吧	
		#逐一导入手动导入测试
#		student_management.import_multi_student(cfg, driver, \
#			base_url, org_name, r"C:\register_user_list.txt")#批量导入学员
#		time.sleep(1)
#		driver.get(current_url)
#		time.sleep(1)
#		student_management.auto_create_student(cfg, driver, \
#			base_url, org_name, stu_num)#批量创建学员
#		time.sleep(1)
#		driver.get(current_url)
#		time.sleep(1)
#		student_management.open_course_for_one(cfg, driver, base_url, org_name)#开通课程
#		time.sleep(1)			
#		student_management.manage_course_num(cfg, driver, base_url, user_name)#管理播放授权数 
#		time.sleep(2)
#		driver.find_element_by_link_text(u"延长授权").click()#延长授权
#		time.sleep(1)
#		driver.find_elements_by_class_name("x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作手动测试 吧													
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的编辑权限" 

	time.sleep(2)
	try:
	    driver.find_element_by_link_text(u"删除学员").click()#删除学员
	    time.sleep(1)
	    driver.find_element_by_css_selector(".x-panel-btns-right .x-btn-text").click()#点击确定
	    time.sleep(1)
	    try:
	        driver.find_element_by_link_text(u"删除帐号").click()
	        time.sleep(1)
	        driver.find_element_by_class_name("x-btn-text").click()#点击确定
	        time.sleep(1)
	    except:
	    	print "没有找到删除帐号"		
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的删除权限"
	  
#网校学员-员工管理
def stuoremp_empmanage():
	time.sleep(2)
	current_url = driver.current_url
	try:
	    driver.find_element_by_link_text(u"筛选").click()#点击筛选
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的读权限"
		return
	
	org_name = "stu_gy"
	user_name = "stu_gy50"
	time.sleep(1)
	try:
		#逐一导入手动导入测试
		driver.find_element_by_link_text(u"批量导入员工").click()#批量导入员工
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"批量创建员工").click()#批量创建员工
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click()
		time.sleep(2)
		driver.find_element_by_link_text(u"开通课程").click()#开通课程
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
		driver.find_element_by_link_text(u"管理播放授权数").click()#管理播放授权数
		time.sleep(1)
		driver.find_element_by_link_text(u"返回").click() 
		time.sleep(1)
#		student_management.open_course_for_one(cfg, driver, base_url, org_name)#开通课程
#		time.sleep(1)
#		student_management.manage_course_num(cfg, driver, base_url, user_name)#管理播放授权数 
#		time.sleep(1)
		driver.find_element_by_link_text(u"延长授权").click()#延长授权
		time.sleep(1)
		driver.find_elements_by_class_name("x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作手动测试 吧													
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的编辑权限" 

	time.sleep(2)
	try:
	    driver.find_element_by_link_text(u"删除员工").click()#删除员工
	    time.sleep(1)
	    driver.find_element_by_css_selector(".x-panel-btns-right .x-btn-text").click()#点击确定
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的删除权限"
	
#网校学员-员工申请
def stuoremp_empapply():
	time.sleep(1)
#	try:
#	    driver.find_element_by_link_text(u"查看资料").click()#点击查看资料
#	    time.sleep(1)
#	except Exception:
#		print traceback.format_exc()
#		print u"没有员工申请的读权限"
#	####加黑名单是什么权限？	
#	time.sleep(1)
#	try:
#		driver.find_element_by_css_selector(".action span").click()#点击通过
#		time.sleep(1)
#		driver.find_elements_by_css_selector(".action span")[1].click()#点击拒绝
#		time.sleep(1)
#	except Exception:
#		print traceback.format_exc()
#		print u"没有员工申请的编辑、删除权限"
			
#网校学员-学员学习记录
def stuoremp_stulearnrecord():
	time.sleep(1)
	current_url = driver.current_url
	try:
		#driver.find_element_by_class_name(".GreenBtn_ab").click()#导出学员学习记录
		time.sleep(1)
		driver.find_element_by_id("J_stuType").click()#选择学员类型
		time.sleep(1)
		driver.find_element_by_css_selector("#J_stuType option").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"查询").click()#点击查询
		time.sleep(1)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"详情").click()#点击详情
		time.sleep(1)
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(1)
		driver.get(current_url)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员学习记录的读、编辑、删除权限"	    		  
   
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

    #后台首页
#	teaching()
#	authmanage()
#	courseagent()
#	learnigcard()
#	countmanage()

    #系统设置

#   #学员/员工
#	stuoremp()

	driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
