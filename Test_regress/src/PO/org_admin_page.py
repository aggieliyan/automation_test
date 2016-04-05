# -*- coding: UTF-8 -*-
'''
Created on Nov. 17, 2014

@author: yilulu
'''
import time

import base
from myoffice_page import MyOfficePage


class OrgAdminListPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_student()
		m.click_org_admin()

	def click_create(self):
		time.sleep(1)
		self.dr.find_element_by_link_text(u"添加管理员").click()

	def click_edit(self):
		time.sleep(1)
		self.dr.find_element_by_link_text(u"编辑管理员").click()

	def click_delete(self, i=-1):
		self.dr.find_elements_by_link_text(u"删除管理员")[i].click()

	def click_delete_ok(self):
		self.dr.find_element(self.cfg.get('org_manage', 'delete_ad_ok_by'), \
			self.cfg.get('org_manage', 'delete_ad_ok')).click()

	def count_admin(self):
		time.sleep(5)
		return len(self.dr.find_elements_by_link_text(u"删除管理员"))
		time.sleep(3)

class OrgAdminInputPage(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def input_name(self, admin_name):
		nameinput =  self.dr.find_element(\
			self.cfg.get('org_manage', 'ad_name_by'), self.cfg.get('org_manage', 'ad_name'))
		nameinput.clear()
		nameinput.send_keys(admin_name)

	def input_username(self, username):
		u_input = self.dr.find_element(self.cfg.get('org_manage', 'ad_username_by'), \
			self.cfg.get('org_manage', 'ad_username'))
		u_input.clear()
		u_input.send_keys(username)

	def input_password(self, password):
		p_input = self.dr.find_element(self.cfg.get('org_manage', 'ad_psw_by'), \
			self.cfg.get('org_manage', 'ad_psw'))
		p_input.clear()
		p_input.send_keys(password)

	def input_psd_again(self, password):
		p_input = self.dr.find_element(self.cfg.get('org_manage', 'ad_repsw_by'), \
			self.cfg.get('org_manage', 'ad_repsw')).send_keys(password)

	def input_email(self, admin_email):
		e_input = self.dr.find_element(self.cfg.get('org_manage', 'ad_email_by'), \
			self.cfg.get('org_manage', 'ad_email'))
		e_input.clear()
		e_input.send_keys(admin_email)

	def input_eml_again(self, admin_email):
		e_input = self.dr.find_element(self.cfg.get('org_manage', 'ad_reemail_by'), \
			self.cfg.get('org_manage', 'ad_reemail'))
		e_input.clear()
		e_input.send_keys(admin_email)

	# def click_look(i):
	# 	#点击第i个
	# 	self.dr.execute_script("$('.onOff').click()")

	def click_add_save(self):
		self.dr.find_element(self.cfg.get('org_manage', 'add_save_by'), \
			self.cfg.get('org_manage', 'add_save')).click()
		time.sleep(1)

	def click_edit_save(self, i=0):
		self.dr.find_elements(self.cfg.get('org_manage', 'edit_save_by'), \
			self.cfg.get('org_manage', 'edit_save'))[i].click()
		time.sleep(1)




