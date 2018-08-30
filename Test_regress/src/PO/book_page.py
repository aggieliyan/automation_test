# -*- coding: UTF-8 -*-
'''
Created on Dec. 03, 2014

@author: yilulu
'''
import time
from selenium.webdriver.support.wait import WebDriverWait
import base
from myoffice_page import MyOfficePage
import random

class BookStepOnrPage(base.Base):


	def __init__(self, driver, cfg):

		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.org_id = cfg.get('env_para', 'org_id')
		self.dr = driver

	def open(self):
		url = "%sbook/toCreate?organizationId=%s"%(self.base_url,self.org_id)
		self.dr.get(url)


	def input_book_title(self, ctitle):
		c_input = self.dr.find_element(self.cfg.get('courseRedirect', 'ctitle_by'), \
			self.cfg.get('courseRedirect', 'ctitle'))
		c_input.clear()
		c_input.send_keys(ctitle)
		time.sleep(0.5)

	def click_service_cate(self):
		self.dr.execute_script("$('li.level2').eq(1).click()")
		self.dr.execute_script("$('li.level3').eq(1).click()")
#		self.dr.execute_script("$('li.level3.selected').click()")
		time.sleep(0.1)
		
#	def click_course_explain(self):
#		self.dr.find_element_by_id("J_agreeBtn").click()
#		time.sleep(0.1)

	#点创建进入下一步
	def click_next_step(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'next_btn_by'), \
			self.cfg.get('courseRedirect', 'next_btn')).click()


#输入教辅信息
class BookInfoPage(base.Base):

	def __init__(self, driver, cfg):
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.org_id = cfg.get('env_para', 'org_id')
		self.dr = driver
	#输入教辅作者
	def input_author(self,b_author):
		b_input=self.dr.find_element(self.cfg.get('courseRedirect', 'book_author_by'), \
			self.cfg.get('courseRedirect', 'book_author'))
		b_input.clear()
		b_input.send_keys(b_author)
		time.sleep(0.5)

	#输入教辅价格
	def input_price(self, cprice):
		time.sleep(1)
		price_orign = self.dr.find_element(self.cfg.get('courseRedirect', 'price_orign_by'), \
			self.cfg.get('courseRedirect', 'price_orign'))
		price_orign.clear()
		price_orign.send_keys(cprice)
		time.sleep(1)
		pinput = self.dr.find_element(self.cfg.get('courseRedirect', 'price_by'), \
			self.cfg.get('courseRedirect', 'price'))
		pinput.clear()
		pinput.send_keys(cprice)

	#选择是否包邮
	def choose_if_mail(self,mark=0):
		#0.包邮   1.不包邮
		if mark>0:

			b_post=self.dr.find_element(self.cfg.get('courseRedirect', 'book_not_post_by'), \
			self.cfg.get('courseRedirect', 'book_not_post'))
			b_post.click()
			#输入基础运费
			baseNum = random.random(1, 10)
			b_baseNum = self.dr.find_element(self.cfg.get('courseRedirect', 'book_baseNum_by'), \
			self.cfg.get('courseRedirect', 'book_baseNum'))
			b_baseNum.clear()
			b_baseNum.sendkeys(baseNum)

			basePrice = random.random(1, 10)
			b_basePrice = self.dr.find_element(self.cfg.get('courseRedirect', 'book_basePrice_by'), \
			self.cfg.get('courseRedirect', 'book_basePrice'))
			b_basePrice.sendkeys(basePrice)
			#输入增加运费
			increaseNum = random.random(1, 10)
			b_increaseNum = self.dr.find_element(self.cfg.get('courseRedirect', 'book_increaseNum_by'), \
			self.cfg.get('courseRedirect', 'book_increaseNum'))
			b_increaseNum.clear()
			b_increaseNum.sendkeys(increaseNum)

			increaseMoney = random.random(1, 10)
			b_increaseMoney = self.dr.find_element(self.cfg.get('courseRedirect', 'book_increaseMoney_by'), \
			self.cfg.get('courseRedirect', 'book_increaseMoney_by'))
			b_increaseMoney.clear()
			b_increaseMoney.sendkeys(increaseMoney)

		else:
			b_post=self.dr.find_element(self.cfg.get('courseRedirect', 'book_is_post_by'), \
			self.cfg.get('courseRedirect', 'book_is_post'))
			b_post.click()

	#保存
	def click_save(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('courseRedirect', 'done_btn_by'), \
			self.cfg.get('courseRedirect', 'done_btn')).click()
		time.sleep(2)


#教辅列表页
class BookListPage(base.Base):

	def __init__(self, driver, cfg):
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		self.org_id = cfg.get('env_para', 'org_id')
		self.dr = driver

	#打开教辅列表页
	def open_list(self):
		bo = MyOfficePage(self.dr, self.cfg)
		bo.open()
		bo.click_teaching()
		bo.click_book()
		time.sleep(2)

	#获取列表第一个图书数据
	def get_data(self):
		try:
			bo1 = self.dr.find_element(self.cfg.get('courseRedirect', 'book_title_by'), \
									   self.cfg.get('courseRedirect', 'book_title')).get_attribute('title')
			return bo1
		except:
			print(u'未定位到图书数据！')

	#删除
	def click_del(self):
		self.dr.find_element(self.cfg.get('courseRedirect', 'book_del_by'), \
			self.cfg.get('courseRedirect', 'book_del')).click()
		time.sleep(1)
		self.dr.find_element(self.cfg.get('courseRedirect', 'book_del_ok_by'), \
			self.cfg.get('courseRedirect', 'book_del_ok')).click()
		time.sleep(2)

