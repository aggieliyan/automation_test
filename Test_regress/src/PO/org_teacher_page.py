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
		m.click_student()
		m.click_teacher()
		#self.dr.implicitly_wait(120)
		time.sleep(120)
		
	def click_createacher(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'create_by'), \
		self.cfg.get('org_teacher', 'create')).click()

	def click_manage(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'manage_by'), \
		self.cfg.get('org_teacher', 'manage')).click()
			        		
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
		time.sleep(1)
				
	def input_name(self, name):
		self.dr.find_element(self.cfg.get('org_teacher', 'name_by'), \
		self.cfg.get('org_teacher', 'name')).send_keys(name)
		time.sleep(3)
	
	def input_recommend(self, commend):
		self.dr.find_element(self.cfg.get('org_teacher', 'recommend_by'), \
		self.cfg.get('org_teacher', 'recommend')).send_keys(commend)
		
	def select_true(self):
		self.dr.find_element_by_css_selector\
		(".select-radio input[data-type='show']").click()
		
	def input_account(self, account):
		self.dr.find_element(self.cfg.get('org_teacher', 'account_by'), \
		self.cfg.get('org_teacher', 'account')).send_keys(account)
		
	def input_password(self, password):
		self.dr.find_element(self.cfg.get('org_teacher', 'password_by'), \
		self.cfg.get('org_teacher', 'password')).send_keys(password)
		
	def input_mail(self, mail):
		self.dr.find_element(self.cfg.get('org_teacher', 'mail_by'), \
		self.cfg.get('org_teacher', 'mail')).send_keys(mail)	
	
	def click_publish(self):
		self.dr.find_element(self.cfg.get('org_teacher', 'publish_by'), \
		self.cfg.get('org_teacher', 'publish')).click()
		
		
	