# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time, random
from selenium import webdriver

import login
import new_course_management
import cate_management, student_management, new_course_management, card_management, user_management
    
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
	menu_dic = {u"我的私信":teaching_letter, 
			       u"网校答疑":teaching_ansquestion,}
	menu_title = u"首页"
	check_menu(menu_title, menu_dic)
			
#后台首页-授权管理
def authmanage():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-授权购买记录、已使用授权 在线购买授权
	menu_dic = {u"授权购买记录":authmanage_buyRecord, 
			       u"已使用授权":authmanage_usegrant,
			       u"在线购买授权":authmanage_buygrant}
	menu_title = u"首页"
	check_menu(menu_title, menu_dic)   

#后台首页-课程合作代理
def courseagent():
	driver.get("%smyOffice.do" %(base_url))
	#教学互动-管理我授权的代理、管理我申请的代理
	menu_dic = {u"管理我授权的代理":agent_grant, 
			    u"管理我申请的代理":agent_apply,}
	menu_title = u"首页"
	check_menu(menu_title, menu_dic)
		
#后台首页-学习卡
def learnigcard():
	driver.get("%smyOffice.do" %(base_url))
	#学习卡-管理卡组、卡使用记录
	menu_dic = {u"管理/卡组":learnigcard_group, 
					       u"卡使用记录":learnigcard_record}
	menu_title = u"首页"
	check_menu(menu_title, menu_dic)

#后台首页-统计管理
def countmanage():
	driver.get("%smyOffice.do" %(base_url))
	#统计管理-外链视频流量统计  浏览量统计 新增学员量统计
	menu_dic = {u"外链视频流量统计":countmanage_outvideo, 
			       u"浏览量统计":countmanage_views,
			       u"新增学员量统计":countmanage_newstudent,}
	menu_title = u"首页"
	check_menu(menu_title, menu_dic)
				     
#系统设置-管理员/客服
def manageorservice():
	driver.get("%smyOffice.do" %(base_url))
	#管理员/客服-网校管理员  网校客服
	menu_dic = {u"网校管理员":manageorservice_manage, 
	               u"网校客服":manageorservice_service,}
	menu_title = u"系统设置"
	check_menu(menu_title, menu_dic)

#系统设置-页面建设
def pagecreate():
	driver.get("%smyOffice.do" %(base_url))
	#页面建设-首页高级编辑  自定义页面  网络图片库  自定义登录图片
	menu_dic = {u"首页高级编辑":pagecreate_edit, 
	               u"自定义页面":pagecreate_selfpage,
	               u"网络图片库":pagecreate_netpic,
	               u"自定义登录图片":pagecreate_selflogin,}
	menu_title = u"系统设置"
	check_menu(menu_title, menu_dic)	
            
#学员/员工-网校学员
def stuoremp():
	driver.get("%smyOffice.do" %(base_url))
	#统计管理-外链视频流量统计  浏览量统计 新增学员量统计
	menu_dic = {u"学员管理":stuoremp_stumanage, 
	                u"员工管理":stuoremp_empmanage,
                    u"学员类目":stuoremp_stucate,
	                #u"员工申请 ":stuoremp_empapply, #手动测试吧
	                u"学员学习记录":stuoremp_stulearnrecord,}
	menu_title = u"学员/员工"
	check_menu(menu_title, menu_dic)
	
#后台首页-教学互动-我的私信
def teaching_letter():
	time.sleep(1)
	try:
		driver.find_element("class name", "x-tab-strip-text").click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的读权限"
		return
	time.sleep(2)	
	try:
        #收件箱发送私信
		driver.find_element("class name", "sendEmialBtn").click()
		time.sleep(1)
		driver.find_element("name", "username").send_keys("stu_gy")
		time.sleep(1)
		driver.find_element("name", "subject").send_keys(u"标题")
		time.sleep(1)
		driver.find_element("name", "msg").send_keys(u"内容")
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btn-td button").click()
		#发件箱发送私信
		time.sleep(1)
		driver.find_element_by_link_text(u"发件箱").click()
		time.sleep(1)
		driver.execute_script("$('#composeMsgTitle').click()")
		#driver.find_element("id", "composeMsgTitle").click()#点击写信  
		time.sleep(1)
		driver.find_element("name", "username").send_keys("gy0411")
		time.sleep(1)
		driver.find_element("name", "subject").send_keys(u"标题")
		time.sleep(1)
		driver.find_element("name", "msg").send_keys(u"内容")
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btn-td button").click()
		time.sleep(1)
		driver.find_element("class name", "x-tab-strip-text").click()#点击收件箱            
	except Exception, e:
		print traceback.format_exc()
		print u"没有我的私信的编辑权限"
        
	time.sleep(2)		
	try:
        #收件箱删除私信
		driver.find_element("class name", "deleteS").click()
		time.sleep(2)
		driver.find_elements("css selector", ".x-panel-btns-center .x-btn-center button")[1].click()
		time.sleep(1)
        #发件箱删除私信
		driver.find_element_by_link_text(u"发件箱").click()
		time.sleep(1)
		driver.find_element("css selector", ".priceAndFeedBGrid .deleteS").click()
		time.sleep(1)
		driver.find_elements("css selector", ".x-window-br .x-btn-text")[1].click()
	except Exception:
		print traceback.format_exc()
		print u"没有我的私信的删除权限"
				 
#后台首页-教学互动-网校答疑    
def teaching_ansquestion():
	time.sleep(1)
	try:
		driver.find_elements("class name", "x-form-arrow-trigger")[0].click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item")[0].click()
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
		
#后台首页-授权管理-授权购买记录	
def authmanage_buyRecord():
	time.sleep(1)
	try:
	    driver.find_element("class name", "cc-arrow").click()#下拉选择
	    time.sleep(1)
	    driver.find_elements("class name", "cc-item")[1].click()
	    time.sleep(2)	
	    driver.find_elements("class name", "j-gldp-target")[0].click()#日期筛选
	    time.sleep(1)    
	    driver.find_element("class name", "outday").click()
	    time.sleep(1)    
	    driver.find_elements("class name", "j-gldp-target")[1].click()
	    time.sleep(1)    
	    driver.find_elements("class name", "outday")[-1].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"查询").click()
	    time.sleep(2)	    
	    driver.find_element_by_link_text(u"购买授权").click()   
	except Exception, e:
	    print traceback.format_exc()
	    print u"没有授权购买记录的读、编辑、删除权限"
	    
#后台首页-授权管理-已使用授权		
def authmanage_usegrant():
	time.sleep(1)
	try:
	    driver.find_element("name", "authType").click()#下拉选择扣除方式
	    time.sleep(1)
	    driver.find_elements("css selector", "select option")[1].click()
	    time.sleep(2)
	    driver.find_element("name", "authStatus").click()#下拉选择状态
	    time.sleep(1)
	    driver.find_elements("css selector", "select option")[-1].click()
	    time.sleep(2)
	    driver.find_elements("class name", "x-form-date-trigger")[0].click()#日期筛选
	    time.sleep(1)
	    driver.find_element("class name", "x-date-active").click()
	    time.sleep(2)	
	    driver.find_elements("class name", "x-form-date-trigger")[1].click()
	    time.sleep(1)    
	    driver.find_elements("class name", "x-date-active")[-1].click()
	    time.sleep(2)
	    driver.find_element("class name", "x-btn-text").click()#点击过滤
	    time.sleep(1)	        
	except Exception:
		print traceback.format_exc()
		print u"没有已使用授权的读、编辑、删除权限"
		
#后台首页-授权管理-在线购买授权	
def authmanage_buygrant():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"在线购买授权").click()   
	except Exception:
		print traceback.format_exc()
		print u"没有在线购买授权的读、删除权限"
		return
#	user_name = 'none'
#	bnum = 1
	current_url = driver.current_url
	time.sleep(1) 
	try:
	    driver.find_element("class name", "authorizeNum").clear()
	    time.sleep(1)
	    driver.find_element("class name", "authorizeNum").send_keys('1')
	    time.sleep(1)		
	    driver.find_element_by_link_text(u"确认购买").click()   
#		student_management.buy_open_num(cfg, driver, base_url, user_name, bnum)
	except Exception:
		print traceback.format_exc()
		print u"没有在线购买授权的编辑权限"
	time.sleep(2)
	driver.get(current_url)

#后台首页-课程合作代理-管理我申请的代理	
def agent_apply():
	courseagent_apply()
	paperagent_apply()

#后台首页-课程合作代理-管理我授权的代理-课程代理
def courseagent_grant():
	time.sleep(1)
	current_url = driver.current_url
	time.sleep(2)
	try:
	    driver.find_element("class name", "agency-navInfo").click()#接受or拒绝
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
		print u"没有管理我授权的代理的课程代理的读、删除权限"
		return

	time.sleep(2) 
	try:
		driver.find_element("class name", "agency-province").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-province option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-city").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-city option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-rank").click()#选择代理级别
		time.sleep(1)
		driver.find_elements("css selector", ".agency-rank option")[2].click()
		time.sleep(1)    
		driver.find_element_by_link_text(u"新建订单").click()#新建订单  
		time.sleep(3)		
		driver.find_elements("name", "categoryItems")[-1].click()
		time.sleep(2)
		driver.find_element("id", "J_acceptProtocol").click()
		time.sleep(2)
		driver.find_element("class name", "x-btn-text").click()#点击发送订单
		time.sleep(2)
		driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
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
		driver.find_element("id", "J_acceptProtocol").click()
		time.sleep(1)
		driver.find_element("class name", "x-btn-text").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
#		driver.get(current_url)
#		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
		time.sleep(1)				  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限"
	time.sleep(2)
	driver.get(current_url)		
#后台首页-课程合作代理-管理我申请的代理-课程代理		
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
		print u"没有管理我申请的代理的课程代理的读、编辑权限"
		return

	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	title = u"agencycourse"+rand_name 
	try:
        #管理课程-编辑课程
		new_course_management.release_agency_course(cfg, driver, base_url, course_title=title)
		driver.get(current_url)
		time.sleep(2)
        #订单管理-立即支付
		driver.find_element_by_link_text(u"订单管理").click()
		bh = driver.window_handles 	  
		time.sleep(1)
		try:
		    driver.find_element_by_link_text(u"立即支付").click()
		except:
			print u"没有立即支付的课程订单"
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(1)
		driver.get(current_url)					  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限"
	time.sleep(2)
	
#后台首页-课程合作代理-管理我授权的代理-考试代理
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
		print u"没有管理我授权的代理的考试代理的读、删除权限"
		return

	time.sleep(2) 
	try:
		driver.find_element("class name", "agency-province").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-province option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-city").click()#选择代理区域
		time.sleep(1)
		driver.find_elements("css selector", ".agency-city option")[2].click()
		time.sleep(1)
		driver.find_element("class name", "agency-rank").click()#选择代理级别
		time.sleep(1)
		driver.find_elements("css selector", ".agency-rank option")[2].click()
		time.sleep(1)    
		driver.find_element_by_link_text(u"新建订单").click()#新建订单 
		time.sleep(2)  
		driver.find_element_by_link_text(u"全选试卷").click()
		time.sleep(2)
		driver.find_element("id", "readed_check").click()
		time.sleep(2)
		driver.find_element("id", "submit_btn").click()
		time.sleep(2)
		driver.find_element("css selector", ".dialog-button-container button").click()#点击确定
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
		driver.find_element("id", "readed_check").click()
		time.sleep(1)
		driver.find_element("id", "submit_btn").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
#		driver.get(current_url)
#		driver.find_element_by_link_text(u"订单管理").click() 
		time.sleep(2)
		driver.find_element_by_link_text(u"取消订单").click()
		time.sleep(1)
		driver.find_element("css selector", ".dialog-button-container button").click()
		time.sleep(1)			  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的考试代理的编辑权限"
	driver.get(current_url)	
	time.sleep(2)
#后台首页-课程合作代理-管理我申请的代理-考试代理
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
		print u"没有管理我申请的代理的考试代理的读、编辑权限"
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
	    driver.find_element("id", "paper_name_input").clear()
	    time.sleep(1)
	    driver.find_element("id", "paper_name_input").send_keys(title)
	    time.sleep(1)
	    driver.find_element("id", "save_btn").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1) 	    
	    driver.find_element_by_link_text(u"订单管理").click()
 	    bh = driver.window_handles  
	    time.sleep(1)
	    try:  
	        driver.find_element_by_link_text(u"立即支付").click()
	    except:
	    	print "没有立即支付的考试订单"
	    ah = driver.window_handles
	    swithing_window(bh,ah)
	    time.sleep(1)				  
	except Exception:
		print traceback.format_exc()
		print u"没有管理我授权的代理的课程代理的编辑权限"
	driver.get(current_url)	
	time.sleep(2)

#后台首页-课程合作代理-管理我授权的代理    
def agent_grant():
    time.sleep(1)
    courseagent_grant()
    paperagent_grant()
    
#后台首页-学习卡-管理卡组
def learnigcard_group():
	time.sleep(1)
	current_url = driver.current_url	
	try:
		driver.find_element_by_link_text(u"浏览卡").click()
		time.sleep(1)
		driver.get(current_url)
		#查看卡组页面-浏览卡
		time.sleep(1)
		driver.find_element("class name","textaligncenter").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"浏览卡").click()
		time.sleep(1)
		#点击该卡组的Excel文件
		time.sleep(1)
		driver.get(current_url)       	
	except Exception:
		print traceback.format_exc()
		print u"没有管理卡组的读权限"
		return
		
	time.sleep(2)	   
	try: 
        #购买试听卡
	    driver.find_element_by_link_text(u"购买试听卡").click()
		#card_management.buy_listen_card(cfg,driver,base_url)#购买试听卡
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
        #查看卡组页面-编辑卡组
	    time.sleep(1)
	    driver.find_element("class name","textaligncenter").click()
	    time.sleep(1)
	    driver.find_element("class name","x-btn-center").click()#点击编辑卡组
	    time.sleep(1)
	    driver.find_elements("class name","x-btn-center")[1].click()#点击保存卡组
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)

        #添加卡组
	    org_name = "stu_lr01"
	    rand_name = str(random.randint(1000, 9999))
	    card_prifix = "auto" + chr(random.randint(97, 122)) + \
	    chr(random.randint(97, 122)) + chr(random.randint(97, 122))
	    
	    group_name = u"prepaidcard"+rand_name
	    group_price = 100
	    card_management.add_prepaid_cardgroup(cfg, driver, base_url, org_name, group_name, group_price)#添加充值卡组
	    card_management.add_card(cfg, driver, base_url, org_name, card_prifix)#添加卡
	    
	    group_name = u"coursecard"+rand_name
	    card_management.add_course_cardgroup(cfg, driver, base_url, org_name, group_name)#添加充课卡组
	    card_management.add_card(cfg, driver, base_url, org_name, card_prifix)#添加卡
	    
	    group_name = u"catecard"+rand_name
	    card_management.add_cate_cardgroup(cfg, driver, base_url, org_name, group_name)#添加补课卡组
	    card_management.add_card(cfg, driver, base_url, org_name, card_prifix)#添加卡
	    
	    group_name = u"listencard"+rand_name        
	    card_management.add_listen_cardgroup(cfg, driver, base_url, org_name, group_name)#添加试听卡组
	    card_management.add_card(cfg, driver, base_url, org_name, card_prifix)#添加卡  
	    
		#driver.find_element_by_link_text(u"添加卡组").click()	
		#time.sleep(1)
		#driver.get(current_url)
		#time.sleep(1)
		#driver.find_element_by_link_text(u"添加卡").click()	
		#time.sleep(1)
		#driver.get(current_url)
        #浏览卡
	    time.sleep(1)
	    driver.find_element_by_link_text(u"浏览卡").click()		
	    time.sleep(1)
	    driver.find_elements("css selector", "input[type=checkbox]")[1].click()#勾选第一个卡
	    time.sleep(1)
        #禁用
	    driver.find_element("class name", "x-form-arrow-trigger").click()#禁用
	    time.sleep(1)
	    driver.find_elements("class name", "x-combo-list-item")[1].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"应用").click()#应用
	    time.sleep(2)
        #启用
	    driver.find_elements("css selector", "input[type=checkbox]")[1].click()#勾选第一卡
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#启用
	    time.sleep(1)	    
	    driver.find_elements("class name", "x-combo-list-item")[2].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"应用").click()#应用
	    time.sleep(1)
        #添加卡
	    driver.find_elements("class name", "colorwhite")[1].click()#点击向该卡组添加卡
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
        #编辑卡组	    
	    driver.find_element_by_link_text(u"编辑卡组").click()#编辑卡组
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#保存修改
	    time.sleep(1)					  
	except Exception, e:
		print traceback.format_exc()
		print u"没有管理卡组的编辑权限"
		
	time.sleep(2)	   
	try:
        #浏览卡页面-删除卡
	    driver.find_element_by_link_text(u"浏览卡").click()		
	    time.sleep(1)
	    driver.find_elements("css selector", "input[type=checkbox]")[1].click()#勾选第一个卡
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#删除
	    time.sleep(1)
	    driver.find_elements("class name", "x-combo-list-item")[0].click()
	    time.sleep(1)
	    driver.find_element_by_link_text(u"应用").click()#应用
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(2)
        #删除卡组
	    driver.find_element_by_link_text(u"删除卡组").click()
	    time.sleep(1)
	    driver.find_elements("css selector", ".x-panel-bwrap .x-btn-text")[5].click()
	    time.sleep(1)
	except Exception, e:
		print traceback.format_exc()
		print u"没有管理卡组的删除权限"
#后台首页-学习卡-卡使用记录	
def learnigcard_record():
	time.sleep(1)
	try:
	    driver.find_element("class name", "x-form-arrow-trigger").click()#下拉选择充卡类型
	    time.sleep(2)
	    driver.find_elements("class name", "x-combo-list-item")[-1].click()
	    time.sleep(1)
	    driver.find_elements("class name", "x-form-date-trigger")[0].click()#日期筛选
	    time.sleep(1)
	    driver.find_element("class name", "x-date-active").click()
	    time.sleep(2)	
	    driver.find_elements("class name", "x-form-date-trigger")[1].click()
	    time.sleep(1)    
	    driver.find_elements("class name", "x-date-active")[-1].click()
	    time.sleep(2)
	    driver.find_element("class name", "x-btn-text").click()#点击过滤
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有卡使用记录的读、编辑、删除权限"

#后台首页-统计管理-外链视频流量统计
def countmanage_outvideo():
	time.sleep(1)
	try:
	    driver.find_element("css selector", "div[data-type=cur-year]").click()#点击本年
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#按日显示
	    time.sleep(2)	
	    driver.find_elements("class name", "x-combo-list-item")[0].click()
	    time.sleep(1)
	    driver.find_element("id", "J_exportExcel").click()#点击导入excel列表
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有外链视频流量统计的读、编辑、删除权限"
		
#后台首页-统计管理-浏览量统计
def countmanage_views():
	time.sleep(1)
	try:
	    driver.find_element("css selector", "span[data-type=recent3month]").click()#点击最近3个月
	    time.sleep(1)
	    driver.find_element("class name", "cc-arrow").click()#按日查询
	    time.sleep(2)	
	    driver.find_elements("class name", "cc-item")[0].click()
	    time.sleep(1)
	    driver.find_element("class name", "exportExecl").click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有浏览量的读、编辑、删除权限"
		
#后台首页-统计管理-新增学员量统计	
def countmanage_newstudent():
	time.sleep(1)
	try:
	    driver.find_element("css selector", "span[data-type=last-month]").click()#点击上个月
	    time.sleep(1)
	    driver.find_element("class name", "cc-arrow").click()#按日查询
	    time.sleep(2)	
	    driver.find_elements("class name", "cc-item")[0].click()
	    time.sleep(1)
	    driver.find_element("class name", "exportExecl").click()
	    time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有新增学员量统计的读、编辑、删除权限"		
 
#系统设置-管理员/客服-网校管理员
def manageorservice_manage():
	time.sleep(1)
	current_url = driver.current_url
	try:
	    driver.find_element("class name","colorGray")#找到编辑管理员的置灰span
	except Exception:
		print traceback.format_exc()
		print u"没有管理员的读权限"

	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"添加管理员").click()
	    time.sleep(1)
	    driver.get(current_url)
	    time.sleep(1)
	    driver.find_element_by_link_text(u"编辑管理员").click()
	    time.sleep(1)
	    driver.get(current_url)	    	    
	except Exception:
		print traceback.format_exc()
		print u"没有管理员的编辑权限"
		
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"删除管理员").click()
	    time.sleep(1)
	    driver.find_element("class name","x-btn-text").click()#删除 
	    time.sleep(1)  	    
	except Exception:
		print traceback.format_exc()
		print u"没有管理员的删除权限"
		
#批量创建读权限管理员
def create_manage_read():
	user_file = open(r"C:/register_admin_user_list_read.txt", 'w')
	i = 1
	pre_name='relog_'
	for item in driver.find_elements("class name","categoryAuthority-look-active"):
		admin_username = create_manage_fillmanage(pre_name, i, user_file)
		time.sleep(1)
		if i != 1:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"保存").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		time.sleep(2)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(2)
	print '读权限管理员个数:' + str(i-1)
	user_file.close()

#批量创建编辑权限管理员
def create_manage_edit():
	user_file = open(r"C:/register_admin_user_list_edit.txt", 'w')    
	i = 1
	pre_name = 'edlog_'
	for item in driver.find_elements("class name", "categoryAuthority-add"):
		admin_username = create_manage_fillmanage( pre_name, i, user_file)
		if i != 1:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"保存").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		driver.implicitly_wait(15)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(1)
	print '编辑权限管理员个数:' + str(i-1)
	user_file.close()

#批量创建删除权限管理员
def create_manage_delete():
	user_file = open(r"C:/register_admin_user_list_delete.txt", 'w')
	i = 1
	pre_name = 'delog_'
	for item in driver.find_elements("class name", "categoryAuthority-delete"):
		admin_username = create_manage_fillmanage(pre_name, i, user_file)
		if i != 1:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"保存").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		driver.implicitly_wait(15)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(1)
	print '删除权限管理员个数' + str(i-1)
	user_file.close()

#批量创建查看、编辑、删除权限管理员
def create_manage_all():
	user_file = open(r"C:/register_admin_user_list_all.txt", 'w')
	i = 1
	pre_name = 'alllog_'
	for item in driver.find_elements("class name", "categoryAuthorityBox"):
		admin_username = create_manage_fillmanage(pre_name, i, user_file)
		if i == 1:
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
		else:
			driver.execute_script("$('.onOff').click()")
			time.sleep(1)
			driver.execute_script("$('.categoryAuthority-look-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-look').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-add-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-add').eq(" + str(i-1) + ").attr('style','display:none'); \
				$('.categoryAuthority-delete-active').eq(" + str(i-1) + ").attr('style','display: inline-block'); \
				$('.categoryAuthority-delete').eq(" + str(i-1) + ").attr('style','display:none')")
		time.sleep(1)
		driver.find_element_by_link_text(u"保存").click()
		time.sleep(1)
		user_file.writelines(admin_username + "\n")
		i = i + 1
		driver.implicitly_wait(15)
		driver.find_element_by_link_text(u"添加管理员").click() 
		time.sleep(1)
	print '查看、编辑、删除权限管理员个数' + str(i-1)
	user_file.close()

#创建管理员填写信息公用方法
def create_manage_fillmanage(pre_name, i, user_file):
	time.sleep(1)
	prefix = chr(random.randint(97, 122)) + chr(random.randint(97, 122)) + chr(random.randint(97, 122))
	admin_name = pre_name + prefix + str(i)
	admin_username = admin_name 
	admin_email = admin_name + "@sohu.com"
	admin_psw = '1234aa'
	time.sleep(1)
	driver.find_element("id", "admin_name").send_keys(admin_name)#管理员名称
	time.sleep(1)
	driver.find_element("id", "admin_username").send_keys(admin_username)#用户名
	time.sleep(1)
	driver.find_element("id", "admin_password").send_keys(admin_psw)#密码
	time.sleep(1)
	driver.find_element("id", "admin_repassword").send_keys(admin_psw)#再次输入密码
	time.sleep(1)
	driver.find_element("id", "admin_email").send_keys(admin_email)#邮箱
	time.sleep(1)
	driver.find_element("id", "admin_reemail").send_keys(admin_email)#再次确认邮箱
	time.sleep(1)
	return admin_username

#创建管理员
def create_manage():
	time.sleep(2)
	driver.get("%smyOffice.do" %(base_url))
	time.sleep(2)
	driver.find_element_by_link_text(u"系统设置").click()   
	time.sleep(2)
	driver.find_element_by_link_text(u"网校管理员").click() 
	time.sleep(2)
	driver.find_element_by_link_text(u"添加管理员").click() 
	time.sleep(2)
	# create_manage_read()#批量创建读权限管理员
	# create_manage_edit()#批量创建编辑权限管理员
	# create_manage_delete()#批量创建删除权限管理员
	create_manage_all()#批量创建读、编辑、删除权限管理员

#系统设置-管理员/客服-网校客服
def manageorservice_service():
	time.sleep(1)
	current_url = driver.current_url
	time.sleep(1)
	try:
	    driver.find_element("class name", "header-cs")#找到网校客服查看网校管理员帮助视频>>
	except Exception:
		print traceback.format_exc()
		print u"没有网校客服的读权限"
	
	time.sleep(2)		
	rand_name = str(random.randint(1000, 9999))
	service_name = u"se" + rand_name
	try:
		#创建机构客服
	    driver.find_element("class name", "toCreatePage").click()#点击创建机构客服
	    time.sleep(1)
	    driver.find_element("class name", "x-form-arrow-trigger").click()#下拉选择用户名
	    time.sleep(1)
	    driver.find_elements("class name", "x-combo-list-item")[1].click()
	    time.sleep(1)
	    driver.find_element("id", "reg_supName").send_keys(service_name)#输入客服名
	    time.sleep(1)
	    driver.find_element("class name", "GreenBtn_ab").click()#点击保存
	    time.sleep(1)
	    #编辑
	    driver.find_elements("css selector", ".supportUl .editSup")[-1].click()#点击编辑  
	    time.sleep(1)
	    driver.find_element("class name", "GreenBtn_ab").click()#点击保存
	    time.sleep(1)
	    #编辑-机构客服显示方式
	    driver.find_element("css selector", ".supportDisplay .editDisplay").click()#点击编辑  
	    time.sleep(1)
	    driver.find_element("class name", "GreenBtn_ab").click()#点击保存
	    time.sleep(1)
	    #选择使用自定义客服-编辑
	    driver.find_elements("name", "customizedSupportEnabled")[1].click()#选择使用自定义客服
	    time.sleep(1)
	    driver.find_element("id", "J_toEditBtn").click()#点击编辑
	    time.sleep(1)	      	    
	    driver.find_element("id", "J_saveCodeBtn").click()#点击保存
	    time.sleep(1)
	    #选择使用AbkeSky机构客服 
	    driver.find_element("name", "customizedSupportEnabled").click()#选择使用AbkeSky机构客服    	    	    	    
	except Exception:
		print traceback.format_exc()
		print u"没有网校客服的编辑权限"
		
	time.sleep(2)
	try:
		#删除
	    driver.find_elements("css selector", ".supportUl .delSup")[-1].click()#点击删除-最后一个创建的机构客服  
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定
	    time.sleep(1)	    
	except Exception:
		print traceback.format_exc()
		print u"没有网校客服的删除权限"	
			
#系统设置-页面建设-首页高级编辑 
def pagecreate_edit():
	time.sleep(1)
	try:
		#预览首页
	    driver.find_elements("class name", "GreenBtn_ab")[-1].click()#点击预览首页
	    time.sleep(1)	    
	except Exception:
		print traceback.format_exc()
		print u"没有首页高级编辑的读、删除权限"	

	time.sleep(1)
	try:
		#发布
	    driver.find_element("class name", "OrangeBtn_ab").click()#点击发布  
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击关闭窗口
	    time.sleep(1)	    
	except Exception:
		print traceback.format_exc()
		print u"没有首页高级编辑的编辑权限"	

#系统设置-页面建设-自定义页面 
def pagecreate_selfpage():
	time.sleep(1)
	try:
		#找到页面html图片
	    driver.find_element("css selector",".floatleft img")
	    time.sleep(1)   
	except Exception:
		print traceback.format_exc()
		print u"没有自定义页面的读权限"
		
	time.sleep(2)
	rand_name = str(random.randint(1000, 9999))
	page_name = u"page" + rand_name	
	try:
		#添加页面
	    driver.find_element("class name", "yellow_btn_center").click()#点击添加页面
	    time.sleep(1)
	    driver.find_element("id", "orgPageField").send_keys(page_name)#页面名称
	    time.sleep(1)
	    driver.find_element("id", "orgWebField").send_keys(rand_name)#为页面设定链接
	    time.sleep(1)
	    driver.find_element("id", "orgInfoField").send_keys("<html><body>hello word!</body></html>")#代码嵌入
	    time.sleep(1)
	    driver.find_elements("class name", "x-btn-text")[-1].click()#点击保存
	    time.sleep(1)
	    #编辑
	    driver.find_element_by_link_text(u"编辑").click()#点击编辑
	    time.sleep(1)
	    driver.find_elements("class name", "x-btn-text")[-1].click()#点击保存
	    time.sleep(1)	    
	    #设为自设导航模块
	    driver.find_element_by_link_text(u"设为自设导航模块").click()#点击设为自设导航模块
	    time.sleep(1)
	    driver.find_element("id", "titleFieldId").send_keys(rand_name)#导航名称
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定
	    time.sleep(1)	    
	    #取消自设导航模块
	    driver.find_element_by_link_text(u"取消自设导航模块").click()#点击取消自设导航模块
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击确定
	    time.sleep(1)	    	    	    
	except Exception:
		print traceback.format_exc()
		print u"没有自定义页面的编辑权限"	

	time.sleep(2)
	try:
		#删除
	    driver.find_element_by_link_text(u"删除").click()#点击删除
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击删除
	    time.sleep(1)    
	except Exception:
		print traceback.format_exc()
		print u"没有自定义页面的删除权限"
			
#系统设置-页面建设-网络图片库 
def pagecreate_netpic():
	time.sleep(1)
	current_url = driver.current_url
	rand_name = str(random.randint(1000, 9999))
	record_name = u"record" + rand_name
	pic = "C:\\Users\\Public\\Pictures\\Sample Pictures\\Tulips.jpg"	
	try:
		#点击第一个图片库
	    driver.find_element("class name", "albumName").click()
	    time.sleep(1)
	    driver.find_element("class name", "albumBg").click()#复制第一个链接   
	    time.sleep(1)
	    driver.find_element_by_link_text(u"返回网络图片库").click()
	    #driver.get(current_url)   
	except Exception:
		print traceback.format_exc()
		print u"没有网络图片库的读权限"
		
	time.sleep(1)
	try:
		#创建专辑
	    driver.find_elements("class name", "cursorHand")[1].click()#点击创建专辑
	    time.sleep(1)
	    driver.find_element("id", "orgAlbumField").send_keys(record_name)#输入专辑名称
	    time.sleep(1)  
	    driver.find_element("id", "picture1").send_keys(pic)#点击浏览上传图片
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击上传
	    time.sleep(2)
	    driver.get(current_url)
	    time.sleep(2)
	    #添加新照片
	    driver.find_element("class name", "albumName").click()#点击选择第一个刚创建的图片库
	    time.sleep(1)
	    current_url = driver.current_url
	    driver.find_element_by_link_text(u"添加新照片").click()
	    time.sleep(1)	    
	    driver.find_element("id", "picture1").send_keys(pic)#点击浏览上传图片
	    time.sleep(1)
	    driver.find_element("class name", "x-btn-text").click()#点击上传 
	    time.sleep(5)
	    driver.get(current_url)
	    #修改专辑名称	    
	    driver.find_element_by_link_text(u"修改专辑名称").click()
	    time.sleep(1)	    
	    driver.find_element("class name", "x-btn-text").click()#点击保存
	    time.sleep(1)  	    
	except Exception:
	    print traceback.format_exc()
	    print u"没有网络图片库的编辑权限"

	time.sleep(2) 
	try:
	    #删除图片
	    try:
	        driver.find_element("class name", "albumName").click()#点击第一个图片库
	        time.sleep(1)
	        driver.find_element("xpath", "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[6]/div[2]").click()
	        time.sleep(1)	    
	        driver.find_element("class name", "x-btn-text").click()#点击确认
	        time.sleep(1)
	    except:
	        print '此专辑么有图片哦'
	    #添加图片--上传图片--删除
	    current_url = driver.current_url
	    driver.find_element_by_link_text(u"添加新照片").click()
	    time.sleep(1)	    
	    driver.find_element("id", "picture1").send_keys(pic)#点击浏览上传图片
	    time.sleep(1)
	    driver.find_element("class name", "deleteAb").click()#点击删除 
	    time.sleep(1)
	    driver.get(current_url)	    
#	    #删除专辑 
#	    driver.find_element_by_link_text(u"删除专辑").click()
#	    time.sleep(1)
#	    driver.find_element("class name","x-btn-text").click()#点击确认-网站有bug，报参数错误    
	except Exception:
		print traceback.format_exc()
		print u"没有网络图片库的删除权限"
	
#系统设置-页面建设-自定义登录图片 
def pagecreate_selflogin():
	time.sleep(1)
	current_url = driver.current_url
	try:
		#能找到第一个的登录图片
	    driver.find_element("id","J_showImage")   
	    time.sleep(1)  
	except Exception:
		print traceback.format_exc()
		print u"没有自定义登录图片的读、删除权限"

	time.sleep(1)
	pic = "C:\\Users\\Public\\Pictures\\Sample Pictures\\1.jpg"
	try:
		#点击浏览
	    time.sleep(1)
	    driver.find_element("id", "picFieldName-file").send_keys(pic)#浏览   
	    time.sleep(1)
	    driver.find_elements("class name", "x-btn-text")[1].click()#上传
	    time.sleep(2)
	    driver.get(current_url)
	    time.sleep(1)
	    #恢复默认
	    driver.find_element("id", "J_restoreDefault").click()
	except Exception:
		print traceback.format_exc()
		print u"没有自定义登录图片的编辑权限"
			
#学员/员工-网校学员-学员类目   
def stuoremp_stucate():
    time.sleep(1)
    current_url = driver.current_url
    try:
        driver.find_element("class name", "expandSub ")#找到展开图标
        time.sleep(1)   
    except Exception:
        print traceback.format_exc()
        print u"没有学员类目的读权限"

    time.sleep(1)
    try:
        driver.find_element("id", "J_genTopCateg").click()#新建一级类目
        creat_stucate()#新建一级类目
        driver.get(current_url)
        bh = driver.window_handles
        manage_catestu(bh)#管理类目学员
        bh = driver.window_handles 
        opencourseBatch(bh)#批量开通课程
        time.sleep(1)
        driver.get(current_url)
        time.sleep(1)
        driver.find_element("class name", "editCateg").click()#编辑类目
        time.sleep(1)
        driver.find_element("class name", "x-btn-text").click()#点击确定        
        time.sleep(1)
        driver.find_element("class name", "addSub").click()#添加子类目
        creat_stucate()
        time.sleep(1)                   
    except Exception:
        print traceback.format_exc()
        print u"没有学员类目的编辑权限"

    time.sleep(2)
    try:
        driver.find_elements("class name", "delete")[-1].click()#删除类目
        time.sleep(1)
        driver.find_element("class name", "x-btn-text").click()#点击删除        
        time.sleep(2)   
    except Exception:
        print traceback.format_exc()
        print u"没有学员类目的删除权限"
    driver.get(current_url)
    time.sleep(2)

#新建一级类目和子类目的方法		
def creat_stucate():
	time.sleep(1)
	rand_name = str(random.randint(1000, 9999))
	cate_name = u"catetest" + rand_name
	try:
	   driver.find_element("id", "reg_topCateName").send_keys(cate_name)#输入类目名称
	except:
	    try:
	        driver.find_element("id", "reg_textField").send_keys(cate_name)#输入类目名称
	    except:
		    None		
	time.sleep(1)
	driver.find_element("class name", "x-btn-text").click()#点击确定			
	time.sleep(1)

#管理类目学员的方法
def manage_catestu(bh):
	time.sleep(3)
	driver.find_element("class name", "manageCategStudent").click()
	ah = driver.window_handles
	swithing_window(bh,ah)
	time.sleep(3)
	driver.find_element_by_link_text(u"添加现有学员").click()
	time.sleep(2)
	driver.find_element_by_link_text(u"全部").click()
	time.sleep(2)
	driver.find_elements("css selector", ".x-panel-bwrap .x-btn-text")[-1].click()
	time.sleep(2)
	driver.find_element_by_link_text(u"返回").click()
	time.sleep(2)

#批量开通课程
def opencourseBatch(bh):
	time.sleep(1)
	driver.find_elements("class name", "openCourseBatch")[0].click()
	time.sleep(3)
	ah = driver.window_handles
	swithing_window(bh,ah)
	driver.find_elements("css selector", "input[type=checkbox]")[-1].click()#勾选最后一个课程类目
	time.sleep(2)
	driver.find_element("class name", "x-btn-text").click()
	time.sleep(2)
	driver.find_elements("css selector", ".x-btn-center .x-btn-text")[1].click()
	time.sleep(3)		
#学员/员工-网校学员-学员管理
def stuoremp_stumanage():
	time.sleep(2)
	current_url = driver.current_url
	try:
		driver.find_element_by_link_text(u"筛选").click()#点击筛选
		time.sleep(1)
		#页面下方批量操作-导出账户信息
		driver.find_element("name","userCheck").click()#勾选第一个学员
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[1].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的读权限"
	
	org_name = "stu_gy"
	user_name = "stu_gy50"
	stu_num = 5
	driver.get(current_url)
	time.sleep(3)
	try:
		driver.find_element_by_link_text(u"批量导入学员").click()#批量导入学员
		time.sleep(2)
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
		driver.find_elements("class name", "x-btn-text")[-1].click()#点击取消
		time.sleep(1)
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
#		driver.find_elements("class name", "x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作-开通课程
		driver.find_element("name","userCheck").click()#勾选第一个学员
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[0].click()
		time.sleep(1)
		driver.get(current_url)
		time.sleep(1)													
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的编辑权限" 

	time.sleep(2)
	try:
		driver.find_element_by_link_text(u"删除学员").click()#删除学员
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btns-right .x-btn-text").click()#点击确定
		time.sleep(1)
		try:
			driver.find_element_by_link_text(u"删除帐号").click()
			time.sleep(1)
			driver.find_element("class name", "x-btn-text").click()#点击确定
			time.sleep(2)
		except:
			print "没有找到删除帐号"
		#页面下方的批量操作-删除员工（删除账号手动测试）
		driver.find_element("name", "userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name", "x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item ")[2].click()
		time.sleep(2)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
		driver.find_element("css selector", ".x-panel-btns-right .x-btn-text").click()#确定		
	except Exception:
		print traceback.format_exc()
		print u"没有学员管理的删除权限"
	  
#学员/员工-网校学员-员工管理
def stuoremp_empmanage():
	time.sleep(2)
	current_url = driver.current_url
	try:
		#筛选
		driver.find_element_by_link_text(u"筛选").click()#点击筛选
		time.sleep(1)
		#页面下方批量操作-导出账户信息
		driver.find_element("name","userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[1].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的读权限"
	
	org_name = "stu_gy"
	user_name = "stu_gy50"
	driver.get(current_url)
	time.sleep(3)
	try:
		#逐一导入手动导入测试
		driver.find_element_by_link_text(u"批量导入员工").click()#批量导入员工
		time.sleep(2)
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
		driver.find_elements("class name", "x-btn-text")[-1].click()#点击取消
		time.sleep(1)
		#页面下方的批量操作-开通课程
		driver.find_element("name","userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name","x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name","x-combo-list-item ")[0].click()
		time.sleep(1)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
		driver.get(current_url)
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的编辑权限" 

	time.sleep(2)
	try:
		driver.find_element_by_link_text(u"删除员工").click()#删除员工
		time.sleep(1)
		driver.find_element("css selector", ".x-panel-btns-right .x-btn-text").click()#删除
		time.sleep(1)
		#页面下方的批量操作-删除员工（删除账号手动测试）
		driver.get(current_url)
		time.sleep(1)
		driver.find_element("name", "userCheck").click()#勾选第一个
		time.sleep(1)
		driver.find_element("class name", "x-form-arrow-trigger").click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item ")[2].click()
		time.sleep(2)
		driver.find_element_by_link_text(u"应用").click()
		time.sleep(2)
		driver.find_element("css selector", ".x-panel-btns-right .x-btn-text").click()#删除
		time.sleep(1)	
	except Exception:
		print traceback.format_exc()
		print u"没有员工管理的删除权限"
	
#学员/员工-网校学员-员工申请
def stuoremp_empapply():
	time.sleep(1)
	try:
	    driver.find_element_by_link_text(u"查看资料").click()#点击查看资料
	    time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有员工申请的读权限"
	####加黑名单是什么权限？	
	time.sleep(1)
	try:
		driver.find_element("css selector", ".action span").click()#点击通过
		time.sleep(1)
		driver.find_elements("css selector", ".action span")[1].click()#点击拒绝
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有员工申请的编辑、删除权限"
			
#学员/员工-网校学员-学员学习记录
def stuoremp_stulearnrecord():
	time.sleep(1)
	current_url = driver.current_url
	try:
		#driver.find_element("class name", ".GreenBtn_ab").click()#导出学员学习记录
		time.sleep(1)
		driver.find_element("id", "J_stuType").click()#选择学员类型
		time.sleep(1)
		driver.find_element("css selector", "#J_stuType option").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"查询").click()#点击查询
		time.sleep(1)
#		driver.find_element("class name", "center").click()#点击导出学员学习记录的excel文件
#		time.sleep(3)
		bh = driver.window_handles
		driver.find_element_by_link_text(u"详情").click()
		time.sleep(1)		
		ah = driver.window_handles
		swithing_window(bh,ah)
		time.sleep(1)    
		driver.find_elements("class name", "centercafC")[3].click()#点击学习记录tab
		time.sleep(2)
		driver.find_element("class name", "x-btn-center").click()#点击过滤
		time.sleep(2)
		driver.find_elements("class name", "cursorHand")[1].click()#点击导出学习记录的excel文件
		time.sleep(1)
		driver.get(current_url)
		time.sleep(1)
	except Exception:
		print traceback.format_exc()
		print u"没有学员学习记录的读、编辑、删除权限"	    		  
   
def admin_athority_check():
    
	global base_url
	global cfg 
	global driver
	base_url = "http://www.gamma.ablesky.com/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file) 

	user_name = "stu_lr01"
	user_psw = "gy0411"

	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()
	driver.maximize_window() #窗口最大化

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
	# driver.get("%smyOffice.do" %(base_url))

	# #后台-先创建管理员	
	# create_manage()

	#后台-后台首页
	# teaching()#教学互动
	# authmanage()#授权管理
	# courseagent()#课程合作代理
	# learnigcard()#学习卡
	# countmanage()#统计管理

	# #后台-系统设置
	manageorservice()#管理员/客服
	# pagecreate()#页面建设

	# #后台-学员/员工
	stuoremp()#网校学员
        
	# driver.quit()
    
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	admin_athority_check()
    