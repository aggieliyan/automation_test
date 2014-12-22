# -*- coding: UTF-8 -*-
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
		time.sleep(1)

	#点击新建试题
	def click_question_create(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_create_by"), \
							self.cfg.get('exam_questions', "question_create")).click()
		time.sleep(1)

	#点击导入试题
	def click_import_questions(self, template):
		self.dr.find_element(self.cfg.get('exam', "import_questions_by"), \
							self.cfg.get('exam', 'import_questions')).click()
		self.dr.execute_script("$('#J_uploadFileInput').attr('style', \
		'height:20px;opacity:1;transform:translate(0px, 0px) scale(1)')")
		time.sleep(1)
		self.dr.find_element(self.cfg.get('exam', "path_by"), \
							self.cfg.get('exam', "path")).send_keys(template)
		self.dr.find_element(self.cfg.get('exam', "upload_button_by"), \
							self.cfg.get('exam', "upload_button")).click()
		time.sleep(2)
		self.dr.find_element(self.cfg.get('exam', "close_button_by"), \
							self.cfg.get('exam', "close_button")).click()										 
	#点击题型的下拉框
	def click_question_type(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_by"), \
							self.cfg.get('exam_questions', "question_type")).click()
		time.sleep(1)
	#多选
   	def click_question_Multiple(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Multiple_by"), \
							self.cfg.get('exam_questions', "question_type_Multiple")).click()
		time.sleep(1)
	#是非
   	def click_question_TrueOrFalse(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_TrueOrFalse_by"), \
							self.cfg.get('exam_questions', "question_type_TrueOrFalse")).click()
		time.sleep(1)
	#问答
   	def click_question_Answer(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Answer_by"), \
							self.cfg.get('exam_questions', "question_type_Answer")).click()
		time.sleep(1)
	#填空
   	def click_question_Blank(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Blank_by"), \
							self.cfg.get('exam_questions', "question_type_Blank")).click()
		time.sleep(1)
	#完型
   	def click_question_Cloze(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Cloze_by"), \
							self.cfg.get('exam_questions', "question_type_Cloze")).click()
		time.sleep(1)
	#综合
   	def click_question_Composite(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_type_Composite_by"), \
							self.cfg.get('exam_questions', "question_type_Composite")).click()
		time.sleep(1)

	#填题目
	def click_question_name(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_name_by"), \
							self.cfg.get('exam_questions', "question_name"))
		time.sleep(1)
		name.click()
		time.sleep(1)
		name.send_keys(question_ansa)
		time.sleep(1)

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
		time.sleep(1)
		name.send_keys(question_ansa)
		time.sleep(1)

		#单选多选答案B
	def click_answerB(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_answerB_by"), \
							self.cfg.get('exam_questions', "question_answerB"))
		name.click()
		time.sleep(1)
		name.send_keys(question_ansa)
		time.sleep(1)

	#问答题答案
	def click_answer_Answer(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_answer_Answer_by"), \
							self.cfg.get('exam_questions', "question_answer_Answer"))
		name.click()
		time.sleep(1)
		name.send_keys(question_ansa)
		time.sleep(1)

	#填空题答案
	def click_Blank_answer(self, question_ansa):
		time.sleep(1)
		self.dr.find_element(self.cfg.get('exam_questions', "question_Blank_by"), \
							self.cfg.get('exam_questions', "question_Blank")).send_keys(question_ansa)
		time.sleep(1)

	#完型题答案
	def click_Cloze1(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze1_by"), \
							self.cfg.get('exam_questions', "question_Cloze1")).send_keys(question_ansa)
		time.sleep(1)
	def click_Cloze2(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze2_by"), \
							self.cfg.get('exam_questions', "question_Cloze2")).send_keys(question_ansa)
		time.sleep(1)
	def click_Cloze3(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze3_by"), \
							self.cfg.get('exam_questions', "question_Cloze3")).send_keys(question_ansa)
		time.sleep(1)
	def click_Cloze4(self, question_ansa):
		self.dr.find_element(self.cfg.get('exam_questions', "question_Cloze4_by"), \
							self.cfg.get('exam_questions', "question_Cloze4")).send_keys(question_ansa)
		time.sleep(1)
							
	#综合题中的单选题名称
	def click_Composite_name(self, question_ansa):
		name = self.dr.find_element(self.cfg.get('exam_questions', "question_Composite_name_by"), \
							self.cfg.get('exam_questions', "question_Composite_name"))
		name.click()
		time.sleep(1)
		name.send_keys(question_ansa)
		time.sleep(1)

	#保存
	def click_question_save(self):
		self.dr.find_element(self.cfg.get('exam_questions', "question_save_by"), \
							self.cfg.get('exam_questions', "question_save")).click()
		time.sleep(1)

