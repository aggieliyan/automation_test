# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: gaoyue
'''
import time

import base
from myoffice_page import MyOfficePage

class OrgCateListPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_org_teach()
		m.click_org_cate()

	def click_create_FirstCate(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'add_topcate_by'), \
            self.cfg.get('org_manage', 'add_topcate')).click()#新建一级类目
        time.sleep(2)

	def input_catename(self, cate_name):
		self.dr.find_element(self.cfg.get('org_manage', 'cate_addname_by'), \
            self.cfg.get('org_manage', 'cate_addname')).send_keys(cate_name)
        time.sleep(2)

	def click_ensure(self):
		self.dr.find_element(self.cfg.get('org_manage', 'add_cate_ok_by'), \
            self.cfg.get('org_manage', 'add_cate_ok')).click()
        time.sleep(3)
			
	def get_lastcatename(self):
		name = self.dr.execute_script("return $(\".categTitle:last\").text()")#取最后一个类目的名称
		return name
			
	def click_delete(self):
		time.sleep(3)
		self.dr.execute_script("$(\".delete:last\").click()")
			
	def click_delete_ok(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'delete_cate_ok_by'), \
            self.cfg.get('org_manage', 'delete_cate_ok')).click()

class OrgcatecoursePge(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open_catecourse(self, cate_num):
		time.sleep(2)
		url_add = self.dr.execute_script("return $('#categoryList .manageCategCourse:eq("+str(cate_num)+")').attr('href')")
		time.sleep(2)
		self.dr.get(self.base_url + str(url_add))

	def click_addcourse_tocate(self):
		time.sleep(5)
		self.dr.find_element_by_link_text(u"向类目添加知识资料").click()

	def select_first(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'course_add_1_by'), \
            self.cfg.get('org_manage', 'course_add_1')).click()

	def get_firstcoursename(self):
		time.sleep(3)
		name = self.dr.execute_script("return $(\"input[name='win_groupCheck']:eq(0)\").parent().parent().next().children().text()")
		return name.strip()
			
	def click_add(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'course_add_ok_by'), \
            self.cfg.get('org_manage', 'course_add_ok')).click()
		time.sleep(3)



