# -*- coding: UTF-8 -*-
'''
Created on Dec. 24, 2014
@author:liuhongjiao
modified on Dec. 24, 2014
@author: yanli
added: click_import_questions
'''

import time
import base
from exam_subject_page import SubjectListPage

class QuestionListPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = SubjectListPage(self.dr, self.cfg)
		m.open()
		m.click_questions()

	#点击新建试题
	def click_question_create(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_create_by"), \
							self.cfg.get('exam_questions', "question_create")).click()
		time.sleep(1)

	#点击导入试题
	def click_import_questions(self, template):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', "import_questions_by"), \
							self.cfg.get('exam', 'import_questions')).click()
		time.sleep(3)
		self.dr.execute_script("$('#J_uploadFileInput').attr('style', \
		'height:20px;opacity:1;transform:translate(0px, 0px) scale(1)')")
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', "path_by"), \
							self.cfg.get('exam', "path")).send_keys(template)
		time.sleep(3)					
		self.dr.find_element(self.cfg.get('exam', "upload_button_by"), \
							self.cfg.get('exam', "upload_button")).click()
		time.sleep(5)
		count = self.dr.execute_script("return $('#J_successImportNum').text()")
		time.sleep(4)
		self.dr.find_element(self.cfg.get('exam', "close_button_by"), \
							self.cfg.get('exam', "close_button")).click()
		time.sleep(2)
		return count	

	#搜索各种题型
	def search_multiple(self):
		self.dr.execute_script("$('#subjectSideBar .normal').eq(1).click()")	
	def search_trueorfalse(self):
		self.dr.execute_script("$('#subjectSideBar .normal').eq(2).click()")
	def search_blank(self):
		self.dr.execute_script("$('#subjectSideBar .normal').eq(3).click()")
	def search_answer(self):
		self.dr.execute_script("$('#subjectSideBar .normal').eq(4).click()")
	def search_cloze(self):
		self.dr.execute_script("$('#subjectSideBar .normal').eq(5).click()")
	def search_composite(self):
		self.dr.execute_script("$('#subjectSideBar .normal').eq(6).click()")
		time.sleep(1)
	#搜索试题
	def search_questions(self, question_ansa):
                time.sleep(2)
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_search_by"), \
							self.cfg.get('exam_questions', "question_search"))
		name.click()
		time.sleep(2)
		name.send_keys(question_ansa)
		time.sleep(2)
		
class QuestionInputPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	#点击题型的下拉框
	def click_question_type(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_by"), \
							self.cfg.get('exam_questions', "question_type")).click()
		time.sleep(1)
	#选择各种题型进行新建试题
	def click_question_multiple(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Multiple_by"), \
							self.cfg.get('exam_questions', "question_type_Multiple")).click()
		time.sleep(1)
	def click_question_trueOrFalse(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_TrueOrFalse_by"), \
							self.cfg.get('exam_questions', "question_type_TrueOrFalse")).click()
		time.sleep(1)
	def click_question_answer(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Answer_by"), \
							self.cfg.get('exam_questions', "question_type_Answer")).click()
		time.sleep(1)
	def click_question_blank(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Blank_by"), \
							self.cfg.get('exam_questions', "question_type_Blank")).click()
		time.sleep(1)
	def click_question_cloze(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Cloze_by"), \
							self.cfg.get('exam_questions', "question_type_Cloze")).click()
		time.sleep(1)
	def click_question_composite(self):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Composite_by"), \
							self.cfg.get('exam_questions', "question_type_Composite")).click()
		time.sleep(1)

	#填题目
	def input_question_name(self, question_ansa):
		time.sleep(2)
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(0).text('" + question_ansa + "')")
		time.sleep(1)

		#添加音频
	def add_music(self):
		self.dr.execute_script("$('.J_audioForm').eq(0).attr('style','display:block;'); \
		$('.file-ie-con input').eq(0).attr('style','height:300px;opacity:1;display:block;position:static;transform:translate(0px, 0px) scale(1)')")
		time.sleep(4)
		self.dr.find_element(self.cfg.get('exam_questions', "question_music_by"), \
							self.cfg.get('exam_questions', "question_music")).send_keys \
							(r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\123.mp3")
		time.sleep(5)

		#单选多选答案ab				
	def input_answerab(self, question_ansa):
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(1).text('" + question_ansa + "')")
		time.sleep(1)
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(2).text('" + question_ansa + "')")
		time.sleep(1)

		#综合题单选多选答案ab				
	def input_com_answerab(self, question_ansa):

		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(2).text('" + question_ansa + "')")
		time.sleep(1)
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(3).text('" + question_ansa + "')")
		time.sleep(1)
		
	#问答题答案
	def input_answer_answer(self, question_ansa):
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(1).text('" + question_ansa + "')")
		time.sleep(1)

	#填空题答案
	def input_blank_answer(self, question_ansa):
		self.dr.execute_script("$('.key').val('" + question_ansa + "')")
        time.sleep(1)

	#完型题答案
	def input_cloze_answer(self, question_ansa):
		self.dr.execute_script("$('.key').val('" + question_ansa + "')")
		time.sleep(2)

	#综合题中的单选题名称
	def input_composite_name(self, question_ansa):
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(0).text('" + question_ansa + "')")
		
		time.sleep(1)
	#综合题中的单选题名称
	def input_composite_small_name(self, question_ansa):
		self.dr.execute_script("$('.J_RICH_TEXTAREA p').eq(1).text('" + question_ansa + "')")
		time.sleep(1)
		
	#保存
	def click_question_save(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_save_by"), \
							self.cfg.get('exam_questions', "question_save")).click()
		time.sleep(3)