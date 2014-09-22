# -*- coding: UTF-8 -*-
import os
import ConfigParser
import traceback
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException

import login
import new_course_management
import cate_management

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
			except UnexpectedAlertPresentException:
				alert = driver.switch_to_alert()
				alert.accept()
			except Exception:
				print traceback.format_exc() 
				error_info = u"没有%s-%s权限"%(menu_title, item)
				print error_info
	except Exception:
		print traceback.format_exc() 
		print u"没有教学教务相关权限"	
#课程类目
def course_cate():
	current_url = driver.current_url
	#修改

	try:
		#新建一级类目
		time.sleep(1)
		cate_management.add_cate(cfg, driver, base_url)
	except:
		print u"不能新建一级类目"

	try:
		#隐藏类目操作
		time.sleep(1)
		driver.find_element("class name", "trueFrame").click()
		#driver.execute_script("$('.trueFrame').eq(0).click()")
		time.sleep(1)
	except:
		print u"不能隐藏类目"

	try:
	    #添加课程到类目中
		cate_management.add_courese_to_cate(cfg, driver, base_url)
		driver.get(current_url)
		time.sleep(1)
	except:
		print u"不能将课程添加到类目"

	try:
		#添加子类目
		driver.find_element("class name", "addSub").click()
		time.sleep(1)
		driver.find_element("id", "reg_textField").clear()
		driver.find_element("id", "reg_textField").send_keys("sub_cate")
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"不能添加子类目"

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
		#发布课程
		driver.get(current_url)
		driver.find_element("class name", "new-categ-button")
		new_course_management.course_redirect(cfg, driver, base_url)
		driver.get(current_url)
	except:
		print traceback.format_exc() 
		print u"不能发布课程"		

	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"获取视频链接").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
	except NoSuchElementException:
		#print traceback.format_exc() 
		print u"不能获取视频链接"

	try:
		#编辑课程
		driver.find_element_by_link_text(u"编辑").click()
		driver.execute_script("$('submit').click()")
		try:
			driver.find_element("id", "J_complete").click()
		except:
			pass
		time.sleep(1)
	except:
		print u"不能编辑课程"

	try:
		#发布相似课程
		driver.get(current_url)
		time.sleep(2)
		driver.find_element_by_link_text(u"发布相似课程").click()
		time.sleep(1)
	except:
		print u"不能发布相似课程"

	try:
		driver.get(current_url)
		alert = driver.switch_to_alert()
		alert.accept()
		time.sleep(3)
		driver.find_element_by_link_text(u"编辑三分屏章节").click()
		time.sleep(1)
	except:
		print u"不能编辑三分屏章节"

	try:
		#员工课程申请
		driver.get(current_url)
		driver.find_element_by_link_text(u"员工课程申请").click()
		driver.find_element_by_link_text(u"通过").click()
		driver.find_element_by_link_text(u"拒绝").click()
	except:
		print u"不能处理员工申请"

	# try:		
	# 	#编辑
	# 	driver.find_element_by_link_text(u"编辑").click()
	# 	driver.execute_script("$('submit').click()")
	# 	try:
	# 		driver.find_element("id", "J_complete").click()
	# 	except:
	# 		pass
	# 	time.sleep(1)

	# 	#发布相似课程
	# 	driver.get(current_url)
	# 	time.sleep(2)
	# 	driver.find_element_by_link_text(u"发布相似课程").click()
	# 	time.sleep(1)

	# 	#编辑三分屏章节
	# 	driver.get(current_url)
	# 	alert = driver.switch_to_alert()
	# 	alert.accept()
	# 	time.sleep(3)
	# 	driver.find_element_by_link_text(u"编辑三分屏章节").click()
	# 	time.sleep(1)

	# 	#发布课程
	# 	driver.get(current_url)
	# 	driver.find_element("class name", "new-categ-button")
	# 	new_course_management.course_redirect(cfg, driver, base_url)

	# 	#员工课程申请
	# 	driver.get(current_url)
	# 	driver.find_element_by_link_text(u"员工课程申请").click()
	# 	driver.find_element_by_link_text(u"通过").click()
	# 	driver.find_element_by_link_text(u"拒绝").click()
	# except NoSuchElementException:
	# 	print traceback.format_exc()
	# 	print u"没有课程编辑权限"

	try:
		#删除
		driver.get(current_url)
		time.sleep(2)
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(2)

		
		#批量删除-手测
		# driver.find_element("id", "J_selAll").click()
		# driver.find_elements("class name", ".cc-textbox")[-1].click()
		# driver.find_element("class name", ".cc-item").click()
		# time.sleep(1)
		# driver.find_element("xpath", "//button").click()

	except NoSuchElementException:
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

	try:
		driver.find_element_by_link_text("添加绑定域名").click()
		time.sleep(1)
		driver.find_element("id", "handleWebInput").send_keys("www.baidu.com")
		driver.find_elements("xpath", "//button")[-2].click()
		time.sleep(1)	
	except:
		print u"不能绑定域名"

	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-2].click()
		time.sleep(1)		
	except:
		print u"不能编辑域名"
    #修改权限
  #   try:
		# driver.find_element_by_link_text("添加绑定域名").click()
		# time.sleep(1)
		# driver.find_element("id", "handleWebInput").send_keys("www.baidu.com")
		# driver.find_elements("xpath", "//button")[-2].click()
        
		# time.sleep(1)
		# driver.find_element_by_link_text(u"编辑").click()
		# time.sleep(1)
		# driver.find_elements("xpath", "//button")[-2].click()
		# time.sleep(1)
  #   except:
		# print traceback.format_exc()
		# print u"没有外链编辑权限"
    #删除
	try:
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-2].click()
		time.sleep(1)
	except:
		print u"没有外链删除权限"

def course_setting():
	try:
		#片头管理
		time.sleep(1)
		driver.find_element("id", "J_showIntroVideo").click()
		driver.find_element("id", "J_allowSkipIntroVideo").click()
		time.sleep(1)
	except:
		print u"不能进行片头管理"

	try:
		#跑马灯
		driver.find_element("id", "editCourseWare").click()
		time.sleep(1)
		driver.find_elements("class name", "bluebtn25_text")[-1].click()
		time.sleep(1)
	except:
		print u"不能设置跑马灯"

def course():
	driver.get("%smyOffice.do" %(base_url))
	menu_dic = {u"课程类目":course_cate,
	            u"课程管理":course_manage,
	            u"课件存储空间":course_space,
	            u'视频外链管理':course_href,
	            u'播放高级设置':course_setting,
	            }
	menu_title = u"教学教务"
	check_menu(menu_title, menu_dic)

def class_manage():
	current_url = driver.current_url

	try:
		#创建网络班
		new_course_management.class_redirect(cfg, driver, base_url, classname='onlineclass', ctype=1)
	except:
		print u"不能创建普通网络班"	
	
	try:
		#编辑
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(3)
		driver.find_element("css selector", "span.greenbtn25_text").click()
	except:
		print u"不能编辑普通网络班"

	try:
		#预售班的创建和编辑
		new_course_management.class_redirect(cfg, driver, base_url, classname='presaleclass', ctype=2)
	except:
		print u"不能创建预售网络班"

	try:
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(3)
		driver.find_element("css selector", "span.greenbtn25_text").click()
	except:
		print u"不能编辑预售网络班"

	try:
		#下架
		time.sleep(1)
		driver.find_element_by_link_text(u"下架").click()
	except:
		print u"不能下架网络班"

	try:
		#上架
		time.sleep(1)
		driver.find_element_by_link_text(u"上架").click()
	except:
		print u"不能上架网络班"

	try:
		#报名详情
		driver.find_element_by_link_text(u"报名详情").click()
		driver.find_element("css selector", "span.greenbtn25_text").click()
		time.sleep(1)
	except:
		print u"不能查看网络班报名详情"
	time.sleep(1)
	#面授班
	driver.get(current_url)
	driver.find_element_by_link_text(u"面授班").click()

	try:
		#创建面授班
		driver.find_element("css selector", "span.greenbtn25_text").click()
		time.sleep(1)
		driver.find_element("id", "J_className").send_keys(u"面授班")
		driver.find_element("classname", "last-price").send_keys("10")
		driver.find_element("name", "class-space").send_keys("1")
		driver.find_element("name", " person-num").send_keys("10")
		#填课程详情
		driver.execute_script("var element=\
			window.document.getElementById('courseDescribe-editor_ifr');\
			idocument=element.contentDocument;\
			element=idocument.getElementById('tinymce');\
			element.innerHTML ='hello';")
		driver.find_element("css selector", \
			"div.text-layer.clearfix > input[type=\"text\"]").send_keys("english\n")
		time.sleep(1)
		#选择服务分类
		driver.execute_script("$(\'li.level2\').click()")
		driver.execute_script("$(\'li.level3.selected\').click()")
		time.sleep(1)
		driver.find_element("css selector", "span.greenbtn25_text").click()
		time.sleep(1)
	except:
		print traceback.format_exc()
		print u"不能创建面授班"
		
	try:
		#编辑
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(3)
		driver.find_element("css selector", "span.greenbtn25_text").click()
	except:
		print traceback.format_exc()
		print u"不能编辑面授班"

	try:
		#下架
		driver.find_element_by_link_text(u"面授班").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"下架").click()
	except:
		print u"不能下架面授班"

	try:
		#报名详情
		driver.find_element_by_link_text(u"报名详情").click()
		time.sleep(1)
		driver.find_element("css selector", "span.greenbtn25_text").click()
		time.sleep(1)		
	except:
		print u"不能查看面授班报名详情"

	try:
		#删除
		driver.get(current_url)
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"不能删除网络班"

	try:
		driver.find_element_by_link_text(u"面授班").click()
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"不能删除预售班"


def class_center():
	driver.get("%smyOffice.do" %(base_url))
	menu_dic = {u"报班管理":class_manage,}
	menu_title = u"教学教务"
	check_menu(menu_title, menu_dic)

def course_test():
	current_url = driver.current_url
	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"查看学员测验详情").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"查看详情").click()
		time.sleep(1)
		driver.get(current_url)
	except:
		print traceback.format_exc() 
		print u"没有课后测验查看权限"


def exam_card():

	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"导出该卡组的Excel文件").click()
		time.sleep(1)
	except:
		print u"没有考试卡查看权限"

	try:
		driver.find_element("id", "J_datatable_batchaction").click()
		time.sleep(1)
		driver.find_element("css selector", "#J_datatable_batchaction > menu > li").click()
		time.sleep(1)
		driver.find_elements("css selector", "input.groupcheck.groupcheck-all")[-1].click()
		driver.find_element("css selector", "a.bluebtn25.apply-batchaction > span.bluebtn25_text").click()
		time.sleep(1)
	except:
		print u"没有考试卡编辑权限"

def exam_system():
	pass

def exam_manage():
	driver.get("%smyOffice.do" %(base_url))
	menu_dic = {u"课后测验报告": course_test,
	               u"考试卡管理": exam_card,
	               u"考试系统":exam_system,}
	menu_title = u"教学教务"
	check_menu(menu_title, menu_dic)

def teacher_manage():
	try:
		time.sleep(1)
		driver.find_element("css selector", "td.text-center > a").click()
	except:
		print u"没有名师管理查看权限"

	try:
		#创建名师
		time.sleep(1)
		driver.find_element_by_link_text(u"创建名师").click()
		time.sleep(1)
		driver.find_element("id", "J_className").send_keys("teacher")
		driver.find_element("id", "courseDescribe-editor").send_keys("teacher introduction")
		driver.find_element("css selector", "span.greenbtn25_text").click()
	except:
		print u"不能创建名师"

	try:
		#编辑
		time.sleep(2)
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(1)
		driver.find_element("css selector", "span.greenbtn25_text").click()
		time.sleep(1)
	except:
		print traceback.format_exc() 
		print u"不能编辑名师"

	try:
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print traceback.format_exc() 
		print u"没有名师删除权限"

def teacher():
	driver.get("%smyOffice.do" %(base_url))
	menu_dic = {u"名师管理": teacher_manage,}
	menu_title = u"教学教务"
	check_menu(menu_title, menu_dic)

def new_onlineclass():
	time.sleep(1)

def onlineclass():
	driver.get("%smyOffice.do" %(base_url))
	menu_dic = {u"发布直播课程": new_onlineclass,}

	menu_title = u"教学教务"
	check_menu(menu_title, menu_dic)

def new_cheapcourse():
	time.sleep(1)

def cheapcourse_manege():
	current_url = driver.current_url
	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"导出表单").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"详情").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"导出表单").click()
		time.sleep(2)
		driver.get(current_url)

		time.sleep(1)
		driver.find_element_by_link_text(u"已下线的团购").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"导出表单").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"详情").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"导出表单").click()
		time.sleep(2)
		driver.get(current_url)	
	except:
		print traceback.format_exc() 
		print u"没有特惠课程查看权限"
    

	try:
		current_url = driver.current_url
		time.sleep(1)
		driver.find_element_by_link_text(u"已下线的团购").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"发布相似团").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-4].click()
		time.sleep(1)
		driver.get(current_url)
	except:
		print u"不能发布相似团"

	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"新建能力团").click()
		time.sleep(1)
		driver.get(current_url)
	except:
		print u"不能新建能力团"
	
	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-2].click()
		time.sleep(1)
	except:
		print u"不能编辑特惠课程"

	try:
		driver.find_element_by_link_text(u"下线").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-2].click()
		time.sleep(1)
	except:
		print traceback.format_exc() 
		print u"不能下线特惠课程"		

def cheap_course():
	driver.get("%smyOffice.do" %(base_url))
	menu_dic = {u"发布特惠课程": new_cheapcourse,
	            u"管理特惠课程": cheapcourse_manege,}
	menu_title = u"教学教务"
	check_menu(menu_title, menu_dic)

def accout_detail():
	current_url = driver.current_url
	try:
		#充值
		driver.find_element_by_link_text(u"立即充值").click()
		time.sleep(1)
		driver.find_element("name", "payment").click()
		driver.find_element("id", "saveBtn").click()
		time.sleep(1)
		driver.get(current_url)
	except:
		print u"没有财务充值权限"

	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"提现").click()
		time.sleep(1)
		driver.find_element("id", "realname").send_keys(u"马如龙")
		driver.find_element("xpath", "//img").click()
		time.sleep(1)
		driver.find_element("class name", "x-combo-list-item").click()
		driver.find_elements("xpath", "//img")[1].click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item")[10].click()
		driver.find_elements("xpath", "//img")[2].click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item")[42].click()
		driver.find_element("id", "banksub").send_keys(u"小英支行")	
		driver.find_element("id", "banknum").send_keys("6225880145880028")
		driver.find_element("id", "banknumretry").send_keys("6225880145880028")
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
		driver.find_element("id", "drawsum").send_keys("1")
		driver.find_elements("xpath", "//button")[1].click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[2].click()
		time.sleep(1)

	except:
		print traceback.format_exc()
		print u"没有提现权限"

	try:
		driver.get(current_url)
		driver.find_element_by_link_text(u"导出收入记录").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"支出").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"导出收入记录").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"充值记录").click()
		driver.find_element_by_link_text(u"提现记录").click()
		driver.find_element_by_link_text(u"转账").click()
	except:
		print u"没有账户明细查看权限"

def accout_charge():
	time.sleep(1)
	driver.find_element("name", "payment").click()
	driver.find_element("id", "saveBtn").click()
	time.sleep(1)

def accout_withdraw():
	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"提现").click()
		time.sleep(1)
		driver.find_element("id", "realname").send_keys(u"马如龙")
		driver.find_element("xpath", "//img").click()
		time.sleep(1)
		driver.find_element("class name", "x-combo-list-item").click()
		driver.find_elements("xpath", "//img")[1].click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item")[10].click()
		driver.find_elements("xpath", "//img")[2].click()
		time.sleep(1)
		driver.find_elements("class name", "x-combo-list-item")[42].click()
		driver.find_element("id", "banksub").send_keys(u"小英支行")	
		driver.find_element("id", "banknum").send_keys("6225880145880028")
		driver.find_element("id", "banknumretry").send_keys("6225880145880028")
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
		driver.find_element("id", "drawsum").send_keys("1")
		driver.find_elements("xpath", "//button")[1].click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[2].click()
		time.sleep(1)

	except:
		print traceback.format_exc()
		print u"没有提现权限"


def member_accout():
	try:
		time.sleep(2)
		toinput = driver.find_elements("css selector", "div.floatleft > input")[1]
		toinput.clear()
		toinput.send_keys("1")
		driver.find_element("xpath", "//a/span[2]").click()
		time.sleep(3)
		driver.find_elements("xpath", "//button")[-1].click()
		time.sleep(2)
	except:
		print traceback.format_exc() 
		print u"没有权限给成员转账"

	try:		
		frominput = driver.find_elements("css selector", "div.floatleft > input")[2]
		frominput.clear()
		frominput.send_keys("1")
		driver.find_element("xpath", "//td[3]/div/div/div[3]/div/a/span[2]").click()
		time.sleep(3)
		driver.find_elements("xpath", "//button")[-1].click()
	except:
		print traceback.format_exc()
		print u"没有权限从成员提账"

def financial():
	driver.get("%smyOffice.do" %(base_url))
	menu_title = u"财务/交易"
	menu_dic = {u"账户明细": accout_detail,    
	            # u"提现": accout_withdraw, 
	            # u"充值": accout_charge,
	            u"管理成员账户": member_accout,}
	check_menu(menu_title, menu_dic)

def sold_history():
	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"导出Excel列表").click()
		time.sleep(1)
		driver.find_element("id", "needpaySellHistory").click()
		time.sleep(1)
		driver.find_element_by_link_text(u"导出Excel列表").click()
		time.sleep(2)
	except:
		print traceback.format_exc() 
		print u"没有卖出交易记录查看权限"

def repay_history():
	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"查看").click()
		time.sleep(1)
	except:
		print traceback.format_exc() 
		print u"没有退款交易记录查看权限"

def transaction():
	driver.get("%smyOffice.do" %(base_url))
	menu_title = u"财务/交易"
	menu_dic = {u"卖出交易记录": sold_history,    
	            u"退款交易记录": repay_history,}
	check_menu(menu_title, menu_dic)

def member_cate():
	try:
		#新建一级类目
		time.sleep(1)
		driver.find_element(cfg.get('org_manage', 'add_topcate_by'), \
    		cfg.get('org_manage', 'add_topcate')).click()
		time.sleep(2)
		driver.find_element(cfg.get('org_manage', 'cate_addname_by'), \
    		cfg.get('org_manage', 'cate_addname')).send_keys("member_cate")
		time.sleep(2)
		driver.find_element(cfg.get('org_manage', 'add_cate_ok_by'), \
    		cfg.get('org_manage', 'add_cate_ok')).click()
		time.sleep(1)
	except:
		print u"不能新建一级成员类目"

	try:
    	#添加子类目
		driver.find_element("class name", "addSub").click()
		time.sleep(1)
		driver.find_element("id", "reg_textField").clear()
		driver.find_element("id", "reg_textField").send_keys("sub_cate")
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"不能添加成员子类目"

	try:
		#编辑类目
		driver.find_element("class name", "editCateg").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print traceback.format_exc() 
		print u"不能编辑成员类目"

    #删除
	try:
		driver.find_elements("class name", "delete")[-1].click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
	except:
		print traceback.format_exc() 
		print u"没有成员类目删除权限"

def member_manage():
	
	time.sleep(1)
	current_url = driver.current_url
	try:
		driver.find_element_by_link_text(u"创建机构成员").click()
		driver.get(current_url)
	except:
		print u"没有创建机构学员权限"

	try:
		time.sleep(1)
		driver.find_element_by_link_text(u"添加类目")
	except:
		print u"没有添加类目的权限"


	try:
		driver.find_element_by_link_text(u"删除成员").click()
		time.sleep(1)
		driver.find_elements("xpath", "//button")[-2].click()
		time.sleep(1)
	except:
		print u"没有删除成员权限"



def member():
	driver.get("%smyOffice.do" %(base_url))
	menu_title = u"其他"
	menu_dic = {u"成员类目": member_cate,    
	            u"成员管理": member_manage,}
	check_menu(menu_title, menu_dic)

def ad_income():
	pass

def ad_manage():
	pass

def ad_system():
	driver.get("%smyOffice.do" %(base_url))
	menu_title = u"其他"
	menu_dic = {u"广告收入记录": ad_income,    
	            u"广告管理": ad_manage,}
	check_menu(menu_title, menu_dic)	

def express_manage():
	try:
		driver.find_element_by_link_text(u"添加快递公司").click()
		time.sleep(1)
		driver.find_element("id", "expressname").send_keys(u"快递公司")
		driver.find_element("id", "expressweb").send_keys("http://www.ablesky.com")
		driver.find_element("xpath", "//button").click()
		time.sleep(2)
	except:
		print u"没有添加快递公司权限"

	try:
		driver.find_element_by_link_text(u"编辑").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(2)
	except:
		print u"没有删除快递公司权限"

	try:
		driver.find_element_by_link_text(u"删除").click()
		time.sleep(1)
		driver.find_element("xpath", "//button").click()
		time.sleep(1)
	except:
		print u"没有删除快递公司权限"


def stu_lecture():
	pass

def course_lecture():
	driver.get("%smyOffice.do" %(base_url))
	menu_title = u"其他"
	menu_dic = {u"管理快递公司": express_manage,    
	            u"管理学员讲义": stu_lecture,}
	check_menu(menu_title, menu_dic)

def admin_athority_check():
    
	global base_url
	global cfg 
	global driver
	base_url = "http://www.gamma.ablesky.com/"
	cfg_file = 'config.ini'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfg_file)
	user_name = "offcn"
	user_psw = "1234"

	chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	#driver = webdriver.Ie()
	driver.maximize_window() #窗口最大化

	login.login_by_logindo(cfg, driver, base_url, user_name, user_psw)
	#教学教务
	course()
	class_center()
	# onlineclass()
	# exam_manage()
	# cheap_course()
	# teacher()

	# #财务/交易39
	# financial()
	# transaction()

	# #其他
	# member()
	# ad_system()
	# course_lecture()

	# driver.quit()
#手测-alllog_hmr27课后测验评分等各种啊
#手册-alllog_wdv44 退款那些


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    admin_athority_check()
