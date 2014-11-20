# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: yilulu
'''
import MyOfficePage
class OrgAdminListPage():

	def __init__(self, driver):
		self.dr = driver
	def open():
		self.dr.get()

	def click_create():
		self.dr.find_element_by_link_text(u"添加管理员").click()

	def click_edit():
		self.dr.find_element_by_link_text(u"编辑管理员").click()

	def clik_delete():
		self.dr.find_elements_by_link_text(u"删除管理员")[-1].click()

class OrgAdminInputPage():
	def __init__(self, driver):
		self.dr = driver

	def input_name(self, admin_name):
		nameinput =  self.dr.find_element(\
			cfg.get('org_manage', 'ad_name_by'), cfg.get('org_manage', 'ad_name'))
		nameinput.clear()
		nameinput.send_keys(admin_name)

	def input_username(self, username):
		u_input = self.dr.find_element(cfg.get('org_manage', 'ad_username_by'), \
			cfg.get('org_manage', 'ad_username'))
		u_input.clear()
		u_input.send_keys(username)

	def input_password(self, password):
		p_input = self.dr.find_element(cfg.get('org_manage', 'ad_psw_by'), \
			cfg.get('org_manage', 'ad_psw'))
		p_input.clear()
		p_input.send_keys(admin_psw)

	def input_psd_again(self, password):
		p_input = self.dr.find_element(cfg.get('org_manage', 'ad_psw_by'), \
			cfg.get('org_manage', 'ad_psw')).send_keys(admin_psw)

	def input_email(self, admin_email):
		e_input = self.dr.find_element(cfg.get('org_manage', 'ad_email_by'), \
			cfg.get('org_manage', 'ad_email'))
		e_input.clear()
		e_input.send_keys(admin_email)

	def input_eml_again(self, admin_email):
		e_input = self.dr.find_element(cfg.get('org_manage', 'ad_reemail_by'), \
			cfg.get('org_manage', 'ad_reemail'))
		e_input.clear()
		e_input.send_keys(admin_email)

	# def click_look(i):
	# 	#点击第i个
	# 	self.dr.execute_script("$('.onOff').click()")

	def click_add_save(self):
		self.find_element(cfg.get('org_manage', 'add_save_by'), \
			cfg.get('org_manage', 'add_save')).click()

	def click_edit_save(self, i=0):
		self.find_elements(cfg.get('org_manage', 'edit_save_by'), \
			cfg.get('org_manage', 'edit_save'))[i].click()




