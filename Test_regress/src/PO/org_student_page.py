# -*- coding: UTF-8 -*-
'''
Created on Dec. 24, 2014
@author:liuhongjiao
'''


import time
import base
from myoffice_page import MyOfficePage

class OrgStudentManagePage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_student()
		m.click_student_management()

	#输入所导入的学员
	def input_studentname(self, stu_name):
		self.dr.find_element_by_id("importBtn").click()
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', "stu_input_by"), \
			self.cfg.get('org_manage', "stu_input")).send_keys(stu_name)
		time.sleep(2)
	#导入
	def click_import(self):
		self.dr.execute_script("$('.dialog-button-container button').eq(0).click()")
		time.sleep(2)
	
    #删除第一个学员并获取用户名供导入使用
	def delete_firstudent(self):
		time.sleep(5)
		self.dr.execute_script("$('li.alt-info-link').eq(0).click()")
		time.sleep(2)
		first_stuname = self.dr.execute_script("return $('.field-title').eq(1).text()")
		time.sleep(2)
		self.dr.execute_script("$('.dialog-button-container button').eq(1).click()")
		time.sleep(2)
		self.dr.execute_script("$('li.del-student-link').eq(0).click()")
		time.sleep(2)
		self.dr.execute_script("$('.dialog-button-container button').eq(0).click()")
		time.sleep(2)
		return first_stuname
			
	#点击批量导入学员
	def click_import_multi(self):
		try:
			self.dr.find_element_by_link_text(u"批量导入学员").click()
		except:
			print '没批量导入学员权限'
	#选择文件
	def click_importchoose(self):
		self.dr.execute_script("$('#fileFieldName-file').attr('style','height:20px;opacity:1;transform:translate(0px, 0px) scale(0.5)')")
	def click_importfile(self, stu_txt):
		self.dr.find_element(self.cfg.get('org_manage', "stu_file_by"), \
			self.cfg.get('org_manage', "stu_file")).send_keys(stu_txt)				
	#导入				
	def click_importmulti(self):
		self.dr.find_element(self.cfg.get('org_manage', "stu_file_ok_by"), \
			self.cfg.get('org_manage', "stu_file_ok")).click()
		time.sleep(2)

	#点击批量创建学员
	def click_create_multi(self):
		time.sleep(5)
		self.dr.find_element_by_id("createBtn").click()
		self.dr.find_element_by_css_selector('#toggle-container > div > div:last-child > input[type="radio"]').click()
	#选择文件
	def click_createchoose(self):
		self.dr.execute_script("$('#fileArea').attr('style','height:20px;opacity:1;transform:translate(0px, 0px) scale(0.5)')")
	def click_createfile(self, stu_txt):
		self.dr.find_element(self.cfg.get('org_manage', "stu_file_by"), \
			self.cfg.get('org_manage', "stu_file")).send_keys(stu_txt)
	#创建
	def click_createmulti(self):
		self.dr.find_element(self.cfg.get('org_manage', "stu_file_ok_by"), \
			self.cfg.get('org_manage', "stu_file_ok")).click()
		self.dr.find_element_by_css_selector("#certainCreateDialog > table > tbody > tr:nth-child(2) > td.td-content > div.dialog-button-container > button").click()
		time.sleep(2)

	#点击开通课程
	def click_open_course(self):
		time.sleep(3)
		bh = self.dr.window_handles
		self.dr.find_element_by_link_text(u"开通移除课程").click()
		time.sleep(3)		
		self.switch_window(bh)
#		self.dr.find_element(self.cfg.get('org_manage', "open_course_by"), \
#			self.cfg.get('org_manage', "open_course")).click()

	#班级开通课程
	#点击进入类目/班级页面
	def click_open_list(self):
		time.sleep(5)
		self.dr.find_element_by_link_text(u"类目/班级").click()
#		self.dr.find_element(self.cfg.get('org_manage', "all_open_list_by"), \
#			self.cfg.get('org_manage', "all_open_list")).click()
		time.sleep(2)
	#选择操作项
	def click_open_choose(self):
		time.sleep(3)
		self.dr.find_elements(self.cfg.get('org_manage', "operation_by"), \
			self.cfg.get('org_manage', "operation"))[0].click()
		time.sleep(2)
	#选择开通/移除课程
	def click_open_check(self):
		time.sleep(2)
		bh = self.dr.window_handles
		self.dr.find_element_by_xpath("//ul[@id='categoryList']/ul/li[1]/span[2]/select/option[4]").click()
		time.sleep(3)
		self.switch_window(bh)
	#应用
#	def click_open_apply(self):
#		self.dr.find_element_by_link_text(u"应用").click()
#		time.sleep(5)

	#开通课程页面
	#未归类内容，展开资料
	def click_opencate(self):
		time.sleep(5)
		self.dr.find_element(self.cfg.get('org_manage', "open_cate_by"), \
			self.cfg.get('org_manage', "open_cate")).click()
		time.sleep(10)
	#选中资料
	def click_openchoose(self):
		self.dr.find_elements(self.cfg.get('org_manage', "open_course_1_by"), \
			self.cfg.get('org_manage', "open_course_1"))[2].click()
		time.sleep(2)
	#选中开通班级里的课程
	def click_class_openchoose(self):
		self.dr.find_elements(self.cfg.get('org_manage', "open_course_2_by"), \
			self.cfg.get('org_manage', "open_course_2"))[2].click()
		time.sleep(2)
	#确认开通
	def click_openok(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', "open_ok_by"), \
			self.cfg.get('org_manage', "open_ok")).click()
		time.sleep(2)
	#弹出框中确认
	def click_opensure(self):
		time.sleep(3)
		self.dr.find_element(self.cfg.get('org_manage', "open_popup_by"), \
			self.cfg.get('org_manage', "open_popup")).click()
		time.sleep(2)
	#有学习进度的确认弹框
	def click_openkeep(self):
		time.sleep(3)
		self.dr.find_elements(self.cfg.get('org_manage', "open_keep_by"), \
			self.cfg.get('org_manage', "open_keep"))[0].click()
		time.sleep(2)
	#开通班级关闭窗口
	def click_openaway(self):
		self.dr.find_element(self.cfg.get('org_manage', "open_away_by"), \
			self.cfg.get('org_manage', "open_away")).click()
		time.sleep(2)

	#管理播放授权数
	#筛选学员user_name
	def click_stu_select(self):
		time.sleep(4)
		self.dr.find_elements(self.cfg.get('manage_course_num', "stu_select_by"), \
							self.cfg.get('manage_course_num', "stu_select"))[0].click()
	def click_stu_selectuser(self):#改xpath
		time.sleep(3)
		self.dr.execute_script("$('ul.cc-itemList li:eq(1)').click()")
#		self.dr.find_elements(self.cfg.get('manage_course_num', "stu_selectuser_by"), \
#							self.cfg.get('manage_course_num', "stu_selectuser")).click()				
	def click_stu_selectinput(self, user_name):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('manage_course_num', 'stu_selectinput_by'), \
							self.cfg.get('manage_course_num', 'stu_selectinput')).send_keys(user_name)
	def click_stu_selectsearch(self):
		self.dr.find_element(self.cfg.get('manage_course_num', "stu_selectsearch_by"), \
							self.cfg.get('manage_course_num', "stu_selectsearch")).click()
		time.sleep(5)
	#点击管理播放授权数
	def click_managenum(self):
		bh = self.dr.window_handles
		self.dr.find_element_by_link_text(u"修改观看次数").click()
		time.sleep(2)		
		self.switch_window(bh)
		time.sleep(3)
	#刷新页面
	def self_dr_refresh(self):
		self.dr.refresh()
		time.sleep(5)
	#批量增加授权数
	def click_coursenum_all(self):
		time.sleep(5)
		self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_all_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_all')).click()
	def click_coursenum_allnum(self):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_allnum_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_allnum')).send_keys("1")
	def click_coursenum_apply(self):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_apply_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_apply')).click()
	#单个课程增加授权数
	#展开资料
	def click_pushcourse(self):
#		self.dr.find_element(self.cfg.get('manage_course_num', "manage_coursenum_opencouse_by"), \
#							self.cfg.get('manage_course_num', "manage_coursenum_opencouse")).click()
		self.dr.find_elements_by_link_text(u"展开课程")[-1].click()     
		time.sleep(3)  
	#展开内容
	def click_pushcontent(self):
#		self.dr.find_element(self.cfg.get('manage_course_num', "manage_coursenum_opennum_by"), \
#							self.cfg.get('manage_course_num', "manage_coursenum_opennum")).click()
		self.dr.find_elements_by_link_text(u"展开内容")[-1].click()  
		time.sleep(2)
	#点击修改剩余播放次数
	def click_changenum(self):
		self.dr.find_elements_by_link_text(u"修改剩余次数")[-1].click()
	def click_course_num(self):
		num = self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_change_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_change'))
		num.clear()
		num.send_keys("1")
	#保存
	def click_save(self):
		self.dr.find_element_by_link_text(u"保存").click()
		self.dr.find_element_by_css_selector('.dialog-button-container button').click()	

	#在线购买授权
	#输入1个授权
	def input_num(self):
		num = self.dr.find_element(self.cfg.get('org_manage', "buy_open_num_input_by"), \
								self.cfg.get('org_manage', "buy_open_num_input"))
		num.click()
		num.clear()
		num.send_keys("1")
	#点击购买
	def click_buy(self):
		self.dr.find_element_by_link_text(u"确认购买").click()
	#确认付款
	def click_sure(self):
		self.dr.find_element_by_link_text(u"去付款").click()
