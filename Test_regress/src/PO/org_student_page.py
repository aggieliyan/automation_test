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
		
	def open_buyopennum(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_num_record()

	#输入所导入的学员
	def input_studentname(self, stu_name):
		self.dr.find_element(self.cfg.get('org_manage', "stu_input_by"), \
			self.cfg.get('org_manage', "stu_input")).send_keys(stu_name)
	#导入
	def click_import(self):
		self.dr.find_element(self.cfg.get('org_manage', "stu_import_btn_by"), \
			self.cfg.get('org_manage', "stu_import_btn")).click()
		time.sleep(2)

	#点击批量导入学员
	def click_import_multi(self):
		self.dr.find_element_by_link_text(u"批量导入学员").click()
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
		self.dr.find_element_by_link_text(u"批量创建学员").click()
	#选择文件
	def click_createchoose(self):
		self.dr.execute_script("$('#fileFieldName-file').attr('style','height:20px;opacity:1;transform:translate(0px, 0px) scale(0.5)')")
	def click_createfile(self, stu_txt):
		self.dr.find_element(self.cfg.get('org_manage', "stu_file_by"), \
			self.cfg.get('org_manage', "stu_file")).send_keys(stu_txt)
	#创建
	def click_createmulti(self):
		self.dr.find_element(self.cfg.get('org_manage', "stu_file_ok_by"), \
			self.cfg.get('org_manage', "stu_file_ok")).click()

	#点击开通课程
	def click_open_course(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', "open_course_by"), \
			self.cfg.get('org_manage', "open_course")).click()
		time.sleep(3)

	#批量开通课程
	#点击下拉框
	def click_open_list(self):
		time.sleep(5)
		self.dr.find_element(self.cfg.get('org_manage', "all_open_list_by"), \
			self.cfg.get('org_manage', "all_open_list")).click()
		time.sleep(2)
	#选择批量开通课程
	def click_open_choose(self):
		self.dr.find_element(self.cfg.get('org_manage', "all_open_by"), \
			self.cfg.get('org_manage', "all_open")).click()
		time.sleep(2)
	#全选
	def click_open_check(self):
		self.dr.find_element(self.cfg.get('org_manage', "all_open_check_by"), \
			self.cfg.get('org_manage', "all_open_check")).click()
		time.sleep(2)
	#应用
	def click_open_apply(self):
		self.dr.find_element_by_link_text(u"应用").click()
		time.sleep(5)

	#开通课程页面
	#未归类内容，展开资料
	def click_opencate(self):
		self.dr.find_element(self.cfg.get('org_manage', "open_cate_by"), \
			self.cfg.get('org_manage', "open_cate")).click()
		time.sleep(10)
	#选中资料
	def click_openchoose(self):
		self.dr.find_element(self.cfg.get('org_manage', "open_course_1_by"), \
			self.cfg.get('org_manage', "open_course_1")).click()
		time.sleep(2)
	#确认开通
	def click_openok(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', "open_ok_by"), \
			self.cfg.get('org_manage', "open_ok")).click()
		time.sleep(2)
	#弹出框中确认
	def click_opensure(self):
		self.dr.find_element(self.cfg.get('org_manage', "open_popup_by"), \
			self.cfg.get('org_manage', "open_popup")).click()
		time.sleep(2)
	#有学习进度的确认弹框
	def click_openkeep(self):
		self.dr.find_element(self.cfg.get('org_manage', "open_keep_by"), \
			self.cfg.get('org_manage', "open_keep")).click()
		time.sleep(2)
	def click_openaway(self):
		self.dr.find_element(self.cfg.get('org_manage', "open_away_by"), \
			self.cfg.get('org_manage', "open_away")).click()
		time.sleep(2)

	#管理播放授权数
	#筛选学员user_name
	def click_stu_select(self):
		time.sleep(5)
		self.dr.find_element(self.cfg.get('manage_course_num', "stu_select_by"), \
							self.cfg.get('manage_course_num', "stu_select")).click()
	def click_stu_selectuser(self):#改xpath
		self.dr.find_element(self.cfg.get('manage_course_num', "stu_selectuser_by"), \
							self.cfg.get('manage_course_num', "stu_selectuser")).click()
	def click_stu_selectinput(self, user_name):
		self.dr.find_element(self.cfg.get('manage_course_num', 'stu_selectinput_by'), \
							self.cfg.get('manage_course_num', 'stu_selectinput')).send_keys(user_name)
	def click_stu_selectsearch(self):
		self.dr.find_element(self.cfg.get('manage_course_num', "stu_selectsearch_by"), \
							self.cfg.get('manage_course_num', "stu_selectsearch")).click()
		time.sleep(5)
	#点击管理播放授权数
	def click_managenum(self):
		self.dr.find_element_by_link_text(u"管理播放授权数").click()
		time.sleep(2)
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
		self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_allnum_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_allnum')).send_keys("1")
	def click_coursenum_apply(self):
		self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_apply_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_apply')).click()
	#单个课程增加授权数
	#展开资料
	def click_pushcourse(self):
		self.dr.find_element(self.cfg.get('manage_course_num', "manage_coursenum_opencouse_by"), \
							self.cfg.get('manage_course_num', "manage_coursenum_opencouse")).click()
	#展开内容
	def click_pushcontent(self):
		self.dr.find_element(self.cfg.get('manage_course_num', "manage_coursenum_opennum_by"), \
							self.cfg.get('manage_course_num', "manage_coursenum_opennum")).click()
	#点击修改剩余播放次数
	def click_changenum(self):
		self.dr.find_element_by_link_text(u"修改剩余播放次数").click()
	def click_course_num(self):
		num = self.dr.find_element(self.cfg.get('manage_course_num', 'manage_coursenum_change_by'), \
							self.cfg.get('manage_course_num', 'manage_coursenum_change'))
		num.clear()
		num.send_keys("1")
	#保存
	def click_save(self):
		self.dr.find_element_by_link_text(u"保存").click()

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
