# -*- coding: UTF-8 -*-
'''
Created on Jul 23, 2014

@author: liwen
'''
import random, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from PO.exam_paper_page import ClickExamSystem, ExamInfoPage, QuestionInfoPage, PaperRecordPage, ScorePage
from PO.base import Base
from PO.random_exam_page import RandomExamPage
from PO.exam_student_page import ExamStudentListPage
from PO.exam_subject_page import SubjectListPage


def create_paper(cfg, driver, base_url, exam_name, exam_time,\
                  eoperation, erandom, eopen):
    """
    operation 代表考试时间结束后操作 0代表默认值，自动交卷
                                 1代表 继续答题
    random 代表试题是否随机排序  0代表 否，不随机排序
                             1代表 是，随机排序
    eopen 代表试卷是否对外开放   0 代表否，不对外开放
                             1代表对外开放
    """
    clickexamsystem = ClickExamSystem(driver,cfg)
    clickexamsystem.open_examsystem()
    
    listpage = SubjectListPage(driver,cfg)
    listpage.click_exampaper()
    listpage.save_screenshot()
        
    examinfo = ExamInfoPage(driver,cfg)
    examinfo.create_paper()
    examinfo.save_screenshot()
    examinfo.input_exam_name(exam_name)
    examinfo.input_exam_time(exam_time)
    examinfo.whether_auto_commit(eoperation)
    examinfo.whether_random(erandom)
    examinfo.open_or_no(eopen)
    examinfo.click_next()
    examinfo.save_screenshot()    
    #添加大题
    auto_creatquestion(cfg, driver, 2)
    time.sleep(3)
    examinfo.save_screenshot()
    #生成试卷
    submit = QuestionInfoPage(driver,cfg)    
    submit.click_submit_btn()
    submit.save_screenshot()
    time.sleep(2)
    return exam_name   
            
#添加大题
def add_big_question(cfg, driver, qscore, qtype):
    """
    qtype表示大题类型，1=单选题，2=多选题，3=是非题，4=填空题，5=问答题，6=完型填空题，7=综合题
    """
    time.sleep(3)
    qinfo = QuestionInfoPage(driver,cfg)
    qinfo.add_big_question(qtype,qscore)
    qinfo.save_screenshot()
    qinfo.exam_import_question()
    time.sleep(3)
    qinfo.save_screenshot()
    
#自动添加题
def auto_creatquestion(cfg, driver, q_num):
    #typel = [1,2,3,4,5,6,7]
    for i in range(q_num):
        qscore = '5'
        qtype = random.randint(1, 7)
        #print qtype
        add_big_question(cfg, driver, qscore, qtype)
   
#随机组卷                        
def random_exam(cfg, driver, base_url, exam_name, exam_time,\
                  eoperation, erandom, eopen):
    clickexamsystem = ClickExamSystem(driver,cfg)
    clickexamsystem.open_examsystem()
    
    listpage = SubjectListPage(driver,cfg)
    listpage.click_exampaper()
    listpage.save_screenshot()
    
    randompg = RandomExamPage(driver,cfg)
    randompg.click_random_btn()
    randompg.save_screenshot()
    
    examinfo = ExamInfoPage(driver,cfg)
    examinfo.input_exam_name(exam_name)
    examinfo.input_exam_time(exam_time)
    examinfo.whether_auto_commit(eoperation)
    examinfo.whether_random(erandom)
    examinfo.open_or_no(eopen)
        
    auto_create_randomquestion(cfg, driver, 1)
    randompg.save_screenshot()
    randompg.click_submit_btn()
    time.sleep(2)
    
#自动添加题
def auto_create_randomquestion(cfg, driver, q_num):
    #typel = [1,2,3,4,5,6,7]
    for i in range(q_num):
#        qscore = '5'
#        qtype = random.randint(1, 7)
        #print qtype
        add_randomq = RandomExamPage(driver,cfg)
        add_randomq.add_question_btn()
        add_randomq.save_screenshot()
        time.sleep(2)
                          
#自动创建试卷
def auto_createpaper(cfg, driver, base_url, eoperation, \
                     erandom, eopen, q_num, exam_num, type):
    ba = Base(driver)
    for i in range(exam_num):
        exam_time = '120'
        if type==1:
            exam_name = 'testpaper_' + ba.rand_name()
            paper_name = create_paper(cfg, driver, base_url, exam_name, exam_time, \
                     eoperation, erandom, eopen)
        else:
            exam_name = 'random_p_' + ba.rand_name()
            paper_name = random_exam(cfg, driver, base_url, exam_name, exam_time,\
                  eoperation, erandom, eopen)
    return paper_name
        #print i      

def exam_result(cfg, driver, base_url, exam_name, etype=1, username=""):
    """
    etype表示需要的操作类型，1为导出分发给学员的试卷统计结果，
                             2为导出作为开放试卷的统计结果,
                             3代表为学员评分
    """
    pp = PaperRecordPage(driver, cfg)
    pp.save_screenshot()
    if not (pp.open(exam_name)):
        return
    pp.click_student_info()
    pp.save_screenshot()

    if etype == 1:
        pp.choose_all_stu()
        pp.output_sendpaper_result()

    elif etype == 2:
        pp.click_open_paper_result()
        pp.choose_all_stu()
        pp.output_opnepaper_result()
        
    else:
        if pp.click_score(username):
            sp = ScorePage(driver, cfg)
            sp.save_screenshot()
            sp.input_score()


def send_close_paper(cfg, driver, base_url, username, atype=2):
    """
    参数atype为1表示为学员开通试卷，2表示为学员关闭试卷
    """
    ep = ExamStudentListPage(driver, cfg)
    ep.open()
    ep.save_screenshot()
    ep.search_student(username)
    if atype == 1:
        ep.click_send_paper()
        ep.save_screenshot()
        ep.choose_all_paper()
    else:
        ep.click_close_paper()
        ep.save_screenshot()
        ep.choose_one_paper()
    ep.click_save()
 
