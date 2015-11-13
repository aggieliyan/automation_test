# -*- coding: UTF-8 -*-
'''
Created on Dec. 24, 2014
@author:liuhongjiao
'''


import time
import base
from myoffice_page import MyOfficePage

class OrgteacherManagePage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_teaching()
		m.click_teacher()
		
	def click_createacher(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'create_by'), \
		self.cfg.get('org_teacher', 'create')).click()
		
	def click_editeacher(self):
		self.dr.find_element_by_link_text(u"编辑").click()
		
	def click_deleteacher(self):
		self.dr.find_element_by_link_text(u"删除").click()
		
	def click_sure(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'delsure_by'), \
		self.cfg.get('org_teacher', 'delsure')).click()

class OrgteacherCreatePage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		
	def clear_name(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'name_by'), \
		self.cfg.get('org_teacher', 'name')).clear()
				
	def input_name(self, name):
		self.dr.find_element(self.cfg.get('org_teacher', 'name_by'), \
		self.cfg.get('org_teacher', 'name')).send_keys(name)
	
	def input_recommend(self, commend):
		self.dr.find_element(self.cfg.get('org_teacher', 'recommend_by'), \
		self.cfg.get('org_teacher', 'recommend')).send_keys(commend)
	
	def click_publish(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'publish_by'), \
		self.cfg.get('org_teacher', 'publish')).click()
	
		
	