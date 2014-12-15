# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: yilulu
'''
import time
import base

class UserpaperListPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = self.cfg.get('env_para', 'base_url')

	def enter_exampaperlist(self):
		self.dr.get(self.base_url+"exam/")

	def clear_searchpapername(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', 'search_input_by'), \
			self.cfg.get('exam', 'search_input')).clear()

	def input_searchpapername(self, paper_name):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', 'search_input_by'), \
			self.cfg.get('exam', 'search_input')).send_keys(paper_name)
			
	def click_examnow(self):
		time.sleep(5)
		self.dr.find_element_by_link_text(u"立即考试").click() 
			

class UserexampaperPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = self.cfg.get('env_para', 'base_url')
		
	def get_examtime(self):
		time.sleep(2)
		exam_time = self.dr.execute_script("return parseInt($('.pre-exam-outer li').eq(0).text().substring(5,6))")
		return exam_time
			
	def click_startexam(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"开始考试").click()		

	def get_questiontitle(self):
		time.sleep(2)
		question_title = self.dr.execute_script("return $('#J_classification a:eq(0)').text()")
		return question_title
	    
	def click_selectquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_selectque_by'), \
			self.cfg.get('exam', 'exam_selectque')).click()
            
	def click_yesnoquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_yesnoque_by'), \
			self.cfg.get('exam', 'exam_yesnoque')).click()   
            
	def click_blankquestion(self, question_answer):
		self.dr.find_element(self.cfg.get('exam', 'exam_blankque_by'), \
			self.cfg.get('exam', 'exam_blankque')).send_keys(question_answer)  
            
	def click_queanswerquestion(self, question_answer):
		iframe_id = self.dr.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
		self.dr.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
		idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
		element.innerHTML =\'"+question_answer+"\';")
            
	def click_clozequestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_clozeque_by'), \
			self.cfg.get('exam', 'exam_clozeque')).click()
            
	def click_all_selectquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_selectque_by'), \
			self.cfg.get('exam', 'exam_all_selectque')).click()
        
	def click_all_yesnoquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_yesque_by'), \
			self.cfg.get('exam', 'exam_all_yesque')).click()       

	def click_all_blankquestion(self, question_answer):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_blankque_by'), \
			self.cfg.get('exam', 'exam_all_blankque')).send_keys(question_answer)
        
	def click_all_queanswerquestion(self, question_answer):
		iframe_id = self.dr.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
		self.dr.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
		idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
		element.innerHTML =\'"+question_answer+"\';") 

	def click_submit(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_submit_by'), \
			self.cfg.get('exam', 'exam_submit')).click()#提交 
            
	def click_confirmsubmit(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', 'exam_continue_by'), \
			self.cfg.get('exam', 'exam_continue')).click()#弹窗-继续考试  
        
	def click_continueexam(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', 'window_submit_by'), \
			self.cfg.get('exam', 'window_submit')).click()#弹窗-提交
