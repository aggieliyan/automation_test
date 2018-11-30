# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: gaoyue
'''
import time
import base
from myoffice_page import MyOfficePage

class UserpaperListPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = self.cfg.get('env_para', 'base_url')
		self.org_id = self.cfg.get('env_para', 'org_id')
		
	def enter_exampaperlist(self):
		url = "%s/studyCenterRedirect.do?action=toStudentExamCenter&orgId=%s&ccgId="%(self.base_url,self.org_id)
		self.dr.get(url)	
	def enter_practice(self):
		self.dr.find_element(self.cfg.get('exam', 'enter_practice_by'), \
			self.cfg.get('exam', 'enter_practice')).click()	      			
	def click_examnow(self):
		time.sleep(7)
		bh = self.dr.window_handles
		try:
			self.dr.find_element_by_link_text(u"答题").click()
		except:
			print u"没有搜索到此名称的试卷"		
		self.switch_window(bh)
	#进入试卷答题页面	
	def click_paper(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"开始答题").click()
#	def clear_searchpapername(self):
#		time.sleep(2)
#		self.dr.find_element(self.cfg.get('exam', 'search_input_by'), \
#			self.cfg.get('exam', 'search_input')).clear()
				
#	def input_searchpapername(self, paper_name):
#		time.sleep(2)		
#		self.dr.find_element(self.cfg.get('exam', 'search_input_by'), \
#			self.cfg.get('exam', 'search_input')).send_keys(paper_name)		
#		time.sleep(0.5)
#        self.dr.find_element(self.cfg.get('exam', 'exam_search_by'), \
#			self.cfg.get('exam', 'exam_search')).click()

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
		time.sleep(3)
		self.dr.find_element_by_link_text(u"开始考试").click()		

	def get_questiontitle(self):
		time.sleep(3)
		question_title = self.dr.execute_script("return $('#totalType').text()")
		return question_title
	
	#点击单选题或多选题中的第一个 
	def click_selectquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_selectque_by'), \
			self.cfg.get('exam', 'exam_selectque')).click()
    
    #点击是非题       
	def click_yesnoquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_yesnoque_by'), \
			self.cfg.get('exam', 'exam_yesnoque')).click()   
    
    #点击填空题        
	def click_blankquestion(self, question_answer):
		self.dr.find_element(self.cfg.get('exam', 'exam_blankque_by'), \
			self.cfg.get('exam', 'exam_blankque')).send_keys(question_answer)
	
	#点击 问答题        
	def click_essayquestion(self, question_answer):
		self.dr.find_element(self.cfg.get('exam', 'exam_essayque_by'), \
			self.cfg.get('exam', 'exam_essayque')).send_keys(question_answer)
    
    #点击问答题        
#	def click_essayquestion(self, question_answer):
#		iframe_id = self.dr.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
#		self.dr.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
#		idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
#		element.innerHTML =\'"+question_answer+"\';")
    
    #点击完形填空题       
	def click_clozequestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_clozeque_by'), \
			self.cfg.get('exam', 'exam_clozeque')).click()
    
    #点击综合题--选择题        
	def click_all_selectquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_selectque_by'), \
			self.cfg.get('exam', 'exam_all_selectque')).click()
    
    #点击综合题-是非题    
	def click_all_yesnoquestion(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_yesque_by'), \
			self.cfg.get('exam', 'exam_all_yesque')).click()       

    #点击综合题-填空题
	def click_all_blankquestion(self, question_answer):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_blankque_by'), \
			self.cfg.get('exam', 'exam_all_blankque')).send_keys(question_answer)
			
	#点击综合题-填空题
	def click_all_essayquestion(self, question_answer):
		self.dr.find_element(self.cfg.get('exam', 'exam_all_essayque_by'), \
			self.cfg.get('exam', 'exam_all_essayque')).send_keys(question_answer)
     
    #点击综合题-问答题   
#	def click_all_essayquestion(self, question_answer):
#		iframe_id = self.dr.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
#		self.dr.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
#		idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
#		element.innerHTML =\'"+question_answer+"\';") 

	def click_submit(self):
		self.dr.find_element(self.cfg.get('exam', 'exam_submit_by'), \
			self.cfg.get('exam', 'exam_submit')).click()#提交 
            
	def click_confirmsubmit(self):
		time.sleep(2)
		self.dr.find_elements(self.cfg.get('exam', 'exam_continue_by'), \
			self.cfg.get('exam', 'exam_continue'))[-1].click()#弹窗-继续考试  
        
	def click_continueexam(self):
		time.sleep(2)
		self.dr.find_elements(self.cfg.get('exam', 'window_submit_by'), \
			self.cfg.get('exam', 'window_submit'))[0].click()#弹窗-提交
