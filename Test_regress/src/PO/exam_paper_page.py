# -*- coding: UTF-8 -*-
'''
Created on Dec 18, 2014

@author: liwen
'''
import base

import time
class ClickExamSystem(base.Base):
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver
        
    def open_examsystem(self):
        url = "%sexam/" %(self.base_url)
        self.dr.get(url)

class  ExamInfoPage(base.Base):
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver    

    def create_paper(self):    
        self.dr.find_element(self.cfg.get('exam', 'exam_subject_by'), \
                        self.cfg.get('exam', 'exam_subject')).click()
        new_href = self.dr.execute_script("return $('.exam-new-btn').attr('href')")
        self.dr.get("%sexam/%s" %(self.base_url,new_href))
    def input_exam_name(self,exam_name):
        input_papername = self.dr.find_element(self.cfg.get('exam', 'exam_paper_name_by'), \
                                        self.cfg.get('exam', 'exam_paper_name'))
        input_papername.clear()
        input_papername.send_keys(exam_name)
                        
    def input_exam_time(self,exam_time):
        input_examtime = self.dr.find_element(self.cfg.get('exam', 'exam_timelen_by'), \
                                        self.cfg.get('exam', 'exam_timelen'))
        input_examtime.clear()
        input_examtime.send_keys(exam_time)
    def whether_auto_commit(self,eoperation):
        if eoperation == 0:
            self.dr.find_element(self.cfg.get('exam', 'exam_operation_auto_by'), \
                                self.cfg.get('exam', 'exam_operation_auto')).click()
        elif eoperation == 1:
            self.dr.find_element(self.cfg.get('exam', 'exam_operation_continue_by'), \
                                self.cfg.get('exam', 'exam_operation_continue')).click()
    def whether_random(self,erandom):
        if erandom == 0:
            self.dr.find_element(self.cfg.get('exam', 'exam_random_false_by'), \
                                self.cfg.get('exam', 'exam_random_false')).click()
        elif erandom == 1:
            self.dr.find_element(self.cfg.get('exam', 'exam_random_true_by'), \
                                self.cfg.get('exam', 'exam_random_true')).click()
    def open_or_no(self,eopen):
        if eopen == 0:
            self.dr.find_element(self.cfg.get('exam', 'exam_open_false_by'), \
                                self.cfg.get('exam', 'exam_open_false')).click()
        elif eopen == 1:
            self.dr.find_element(self.cfg.get('exam', 'exam_open_true_by'), \
                                self.cfg.get('exam', 'exam_open_true')).click()
            self.dr.find_element(self.cfg.get('exam', 'exam_times_down_by'), \
                                self.cfg.get('exam', 'exam_times_down')).click()
            self.dr.find_element(self.cfg.get('exam', 'exam_times_by'), \
                                self.cfg.get('exam', 'exam_times')).click()
                            
            paper_price = self.dr.find_element(self.cfg.get('exam', 'exam_paper_price_by'), \
                            self.cfg.get('exam', 'exam_paper_price'))
            paper_price.clear()
            paper_price.send_keys("10")
    def click_next(self):
        self.dr.find_element(self.cfg.get('exam', 'exam_next_one_by'), \
                        self.cfg.get('exam', 'exam_next_one')).click()
class QuestionInfoPage(base.Base):
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver
    
    def add_big_question(self,qtype,qscore):
        self.dr.find_element(self.cfg.get('exam', 'paper_add_big_question_by'), \
                        self.cfg.get('exam', 'paper_add_big_question')).click()
        self.dr.implicitly_wait(1)
        if qtype == 1:
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_dropdown_by'), \
                            self.cfg.get('exam', 'exam_topic_dropdown')).click()
            self.dr.find_element('xpath', '//div[10]/ul/li').click()
        else:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_dropdown_by'), \
                            self.cfg.get('exam', 'exam_topic_dropdown')).click()
            self.dr.implicitly_wait(10)
        if qtype == 2:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_multiple_by'), \
                                self.cfg.get('exam', 'exam_topic_multiple')).click()
        if qtype == 3:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', \
                                        'exam_topic_true_or_false_by'), \
                                self.cfg.get('exam', \
                                        'exam_topic_true_or_false')).click()
            time.sleep(2)
        if qtype == 4:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_fills_by'), \
                                self.cfg.get('exam', 'exam_topic_fills')).click()
            self.dr.implicitly_wait(10)
        if qtype == 5:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_question_by'), \
                                self.cfg.get('exam', 'exam_topic_question')).click()
            time.sleep(2)
        if qtype == 6:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_cloze_by'), \
                                self.cfg.get('exam', 'exam_topic_cloze')).click()
            time.sleep(2)
        if qtype == 7:
            time.sleep(2)
            self.dr.find_element(self.cfg.get('exam', \
                                        'exam_topic_comprehensive_by'), \
                                self.cfg.get('exam', \
                                        'exam_topic_comprehensive')).click()
            time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'exam_question_score_by'), \
                                     self.cfg.get('exam', 'exam_question_score')).click()
        self.dr.find_element(self.cfg.get('exam', 'exam_question_score_by'), \
                        self.cfg.get('exam', 'exam_question_score')).clear()
        self.dr.find_element(self.cfg.get('exam', 'exam_question_score_by'), \
                        self.cfg.get('exam', \
                                'exam_question_score')).send_keys(qscore)
        self.dr.find_element(self.cfg.get('exam', 'exam_add_big_question_ok_by'), \
                        self.cfg.get('exam', 'exam_add_big_question_ok')).click()        
    
    def exam_import_question(self):
        self.dr.find_element(self.cfg.get('exam', 'paper_import_question_by'), \
                        self.cfg.get('exam', 'paper_import_question')).click()
        self.dr.find_element(self.cfg.get('exam', 'paper_selece_all_by'), \
                        self.cfg.get('exam', 'paper_selece_all')).click()
        time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'exam_add_big_question_ok_by'), \
                        self.cfg.get('exam', 'exam_add_big_question_ok')).click()
    def click_submit_btn(self):
        self.dr.find_element(self.cfg.get('exam', 'exam_paper_build_btn_by'), \
                        self.cfg.get('exam', 'exam_paper_build_btn')).click()