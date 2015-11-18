
# -*- coding: UTF-8 -*-
'''
Created on Dec 18, 2014

@author: liwen

modified on Dec. 24, 2014
@author:yilulu
added: PaperListPage
       PaperRecordPage
       ScorePage

'''

import time

import base
from PO.exam_subject_page import SubjectListPage

class PaperListPage(base.Base):


    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver

    def click_creat_paper(self):
        pass

    def search_paper(self, paper_name):
        self.dr.find_element(self.cfg.get('exam', 'paper_search_by'), \
            self.cfg.get('exam', 'paper_search')).send_keys(paper_name)
        time.sleep(1)
    
    #点击试卷名称
    def click_paper(self, exam_name):
        exam_href = self.dr.execute_script(\
            "return $(\"a:contains(\'"+exam_name+"\')\").attr('href')")
        time.sleep(1)
        if exam_href:
            self.dr.get("%sexam/%s" % (self.base_url, exam_href))
            return 1
        else:
            print u"no paper named ",exam_name
            return 0
        

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
        time.sleep(1)    
        self.dr.find_element(self.cfg.get('exam', 'exam_subject_by'), \
                        self.cfg.get('exam', 'exam_subject')).click()
        time.sleep(1) 
        new_href = self.dr.execute_script("return $('.exam-new-btn').attr('href')")
        time.sleep(2) 
        self.dr.get("%sexam/%s" %(self.base_url,new_href))

    def input_exam_name(self,exam_name):
        time.sleep(3)
        input_papername = self.dr.find_element(self.cfg.get('exam', 'exam_paper_name_by'), \
                                        self.cfg.get('exam', 'exam_paper_name'))
        time.sleep(1)
        input_papername.clear()
        time.sleep(1)
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
            time.sleep(1)
            self.dr.find_element(self.cfg.get('exam', 'exam_open_false_by'), \
                                self.cfg.get('exam', 'exam_open_false')).click()
        elif eopen == 1:
            time.sleep(1)
            self.dr.find_element(self.cfg.get('exam', 'exam_open_true_by'), \
                                self.cfg.get('exam', 'exam_open_true')).click()
            time.sleep(1)
            self.dr.find_elements(self.cfg.get('exam', 'exam_times_down_by'), \
                                self.cfg.get('exam', 'exam_times_down'))[-1].click()
            time.sleep(1)              
            self.dr.find_element(self.cfg.get('exam', 'exam_times_by'), \
                                self.cfg.get('exam', 'exam_times')).click()
            time.sleep(1)                    
            paper_price = self.dr.find_element(self.cfg.get('exam', 'exam_paper_price_by'), \
                            self.cfg.get('exam', 'exam_paper_price'))
            paper_price.clear()
            paper_price.send_keys("10")
    def click_next(self):
        time.sleep(1)
        self.dr.find_element(self.cfg.get('exam', 'exam_next_one_by'), \
                        self.cfg.get('exam', 'exam_next_one')).click()
class QuestionInfoPage(base.Base):
    
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver
    
    def add_big_question(self,qtype,qscore):
        time.sleep(4)
        self.dr.find_element(self.cfg.get('exam', 'paper_add_big_question_by'), \
                        self.cfg.get('exam', 'paper_add_big_question')).click()
        if qtype == 1:
            time.sleep(4)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_dropdown_by'), \
                            self.cfg.get('exam', 'exam_topic_dropdown')).click()
            time.sleep(2)                
            self.dr.find_element('xpath', '//div[10]/ul/li').click()
        else:
            time.sleep(4)
            self.dr.find_element(self.cfg.get('exam', 'exam_topic_dropdown_by'), \
                            self.cfg.get('exam', 'exam_topic_dropdown')).click()
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
        time.sleep(1)
        self.dr.find_element(self.cfg.get('exam', 'exam_add_big_question_ok_by'), \
                        self.cfg.get('exam', 'exam_add_big_question_ok')).click()        
    
    def exam_import_question(self):
        time.sleep(1)
        self.dr.find_element(self.cfg.get('exam', 'paper_import_question_by'), \
                        self.cfg.get('exam', 'paper_import_question')).click()
        time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'paper_selece_all_by'), \
                        self.cfg.get('exam', 'paper_selece_all')).click()
        time.sleep(2)
        self.dr.find_element(self.cfg.get('exam', 'exam_add_big_question_ok_by'), \
                        self.cfg.get('exam', 'exam_add_big_question_ok')).click()
    def click_submit_btn(self):
        time.sleep(6)
        self.dr.find_element(self.cfg.get('exam', 'exam_paper_build_btn_by'), \
                        self.cfg.get('exam', 'exam_paper_build_btn')).click()
        time.sleep(2)

#点击试卷标题进入的页面 里面有试卷信息、试题信息、学员信息和试题统计
class PaperRecordPage(base.Base):

    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver

    def open(self, exam_name):
        sp = SubjectListPage(self.dr, self.cfg)
        sp.open()
        sp.click_exampaper()
        pp = PaperListPage(self.dr, self.cfg)
        pp.search_paper(exam_name)
        return pp.click_paper(exam_name)

    def click_student_info(self):
        self.dr.find_element_by_link_text("学员信息").click()

    #在学员信息统计结果那全选
    def choose_all_stu(self):
        try:
            self.dr.find_element(self.cfg.get('exam', 'select_stu_by'), \
                self.cfg.get('exam', 'select_stu')).click()
        except Exception, e:
            print u"统计结果列表为空"

    #导出分发给学员试卷的结果
    def output_sendpaper_result(self):
        try:
            self.dr.find_element(self.cfg.get('exam', 'output_by'), \
                self.cfg.get('exam', 'output')).click()
            time.sleep(2)
        except:
            print u'试卷暂时没有分发给学员'

    def click_open_paper_result(self):
        self.dr.find_element_by_link_text(u"作为开放试卷的统计结果").click()

    #导出开放试卷的统计结果
    def output_opnepaper_result(self):
        try:
            self.dr.find_element(self.cfg.get('exam', 'output_open_by'), \
                self.cfg.get('exam', 'output_open')).click()
            time.sleep(2)
        except:
            print u"还没有学员购买该试卷"

    #点击某个学员后面的去评分
    def click_score(self, username):
        stu_name = self.dr.execute_script(\
            "return $(\"a:contains(\'"+username+"\')\").parents('.odd').children().eq(0).children().text()")
        time.sleep(1)
        if username not in stu_name:
            print username + u'该学员不存在,无法评分。。'
            return 0

        grade_href = self.dr.execute_script(\
            "return $(\"a:contains(\'"+username+"\')\").parents('.odd').children().eq(5).children().attr('href')")
        time.sleep(2)
        if not grade_href:
            print u"学员尚未提交试卷"
            return 0
        self.dr.get("%sexam/%s" % (self.base_url, grade_href))
        return 1

class ScorePage(base.Base):


    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver

    #评分并返回总分
    def input_score(self, score="0.1"):
        score_input = self.dr.find_elements(self.cfg.get('exam', 'input_score_by'), \
            self.cfg.get('exam', 'input_score'))
        count = 0
        for item in score_input:
            try:
                item.clear()
                item.send_keys(score)
                count += 1
            except:
                continue

        return count * score
        
    def click_save(self):
        self.dr.find_element(self.cfg.get('exam', 'score_save_by'), \
            self.cfg.get('exam', 'score_save')).click()
        time.sleep(1)