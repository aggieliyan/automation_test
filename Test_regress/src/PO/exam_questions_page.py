# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: yilulu
'''
import time

import base
from myoffice_page import MyOfficePage


class ExamQuestions(base.Base):


	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.click_exam()

    #点击试题库
	def click_questions(self):
		self.dr.find_element_by_link_text(u"试题库").click()

	#点击新建试题
	def click_question_creat(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_creat_by"), \
							self.cfg.get('exam_questions', "question_creat")).click()

    #点击题型的下拉框
	def click_question_type(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_by"), \
							self.cfg.get('exam_questions', "question_type")).click()
    #多选
   	def click_question_Multiple(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Multiple_by"), \
							self.cfg.get('exam_questions', "question_type_Multiple")).click()
    #是非
   	def click_question_TrueOrFalse(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_TrueOrFalse_by"), \
							self.cfg.get('exam_questions', "question_type_TrueOrFalse")).click()
	#问答
   	def click_question_Answer(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Answer_by"), \
							self.cfg.get('exam_questions', "question_type_Answer")).click()
	#填空
   	def click_question_Blank(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Blank_by"), \
							self.cfg.get('exam_questions', "question_type_Blank")).click()
	#完型
   	def click_question_Cloze(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Cloze_by"), \
							self.cfg.get('exam_questions', "question_type_Cloze")).click()
	#综合
   	def click_question_Composite(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Composite_by"), \
							self.cfg.get('exam_questions', "question_type_Composite")).click()

	#填题目
	def click_question_name(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_name_by"), \
							self.cfg.get('exam_questions', "question_name"))
		name.click()
		name.send_keys(question_ansa)

    #添加音频
	def click_music(self):
		self.dr.execute_script("$('.J_audioForm').eq(0).attr('style','display:block;'); \
		$('.file-ie-con input').eq(0).attr('style','height:300px;opacity:1;display:block;position:static;transform:translate(0px, 0px) scale(1)')")
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam_questions', "question_music_by"), \
							self.cfg.get('exam_questions', "question_music")).send_keys \
							(r"\\data.ablesky.com\workspace\Testing\Testing Files\Automation_test\123.mp3")
		time.sleep(2)

    #单选多选答案A				
	def click_answerA(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_answerA_by"), \
							self.cfg.get('exam_questions', "question_answerA"))
		name.click()
		name.send_keys(question_ansa)

    #单选多选答案B
	def click_answerB(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_answerB_by"), \
							self.cfg.get('exam_questions', "question_answerB"))
		name.click()
		name.send_keys(question_ansa)
		time.sleep(2)

	#问答题答案
	def click_answer_Answer(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_answer_Answer_by"), \
							self.cfg.get('exam_questions', "question_answer_Answer"))
		name.click()
		name.send_keys(question_ansa)
		time.sleep(2)

	#填空题答案
	def click_Blank_answer(self, question_ansa):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam_questions', "question_Blank_by"), \
							self.cfg.get('exam_questions', "question_Blank")).send_keys(question_ansa)
		time.sleep(2)

	#完型题答案
	def click_Cloze1(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze1_by"), \
							self.cfg.get('exam_questions', "question_Cloze1")).send_keys(question_ansa)
	def click_Cloze2(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze2_by"), \
							self.cfg.get('exam_questions', "question_Cloze2")).send_keys(question_ansa)
	def click_Cloze3(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze3_by"), \
							self.cfg.get('exam_questions', "question_Cloze3")).send_keys(question_ansa)
	def click_Cloze4(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze4_by"), \
							self.cfg.get('exam_questions', "question_Cloze4")).send_keys(question_ansa)
							
	#综合题中的单选题名称
	def click_Composite_name(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_Composite_name_by"), \
							self.cfg.get('exam_questions', "question_Composite_name"))
		name.click()
		name.send_keys(question_ansa)
		time.sleep(2)

	#保存
	def click_question_save(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_save_by"), \
							self.cfg.get('exam_questions', "question_save")).click()

