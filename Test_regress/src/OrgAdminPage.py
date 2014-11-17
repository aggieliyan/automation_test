# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: yilulu
'''
class OrgAdminListPage():

	def __init__(self, driver):
		self.dr = driver

	def click_create():
		self.dr.find_element_by_link_text(u"添加管理员").click()

	def click_edit():
		self.dr.find_element_by_link_text(u"编辑管理员").click()

	def clik_delete():
		self.dr.find_elements_by_link_text(u"删除管理员")[-1].click()

class OrgAdminInputPage():
	def __init__(self, driver):
		self.dr = driver

	def input_name(admin_name):
		nameinput =  self.dr.find_element(\
			cfg.get('org_manage', 'ad_name_by'), cfg.get('org_manage', 'ad_name'))
		nameinput.clear()
		nameinput.send_keys(admin_name)

	def input_username(username):
		u_input = driver.find_element(cfg.get('org_manage', 'ad_username_by'), \
			cfg.get('org_manage', 'ad_username'))
		u_input.clear()
		u_input.send_keys(username)

	def input_password(password):
		p_input = driver.find_element(cfg.get('org_manage', 'ad_psw_by'), \
			cfg.get('org_manage', 'ad_psw'))
		p_input.clear()
		p_input.send_keys(admin_psw)

	def input_psd_again(password):
		p_input = driver.find_element(cfg.get('org_manage', 'ad_psw_by'), \
			cfg.get('org_manage', 'ad_psw')).send_keys(admin_psw)

