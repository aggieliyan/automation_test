# -*- coding: UTF-8 -*-
'''
Created on Jul 23, 2014

@author: liwen
'''

from selenium.webdriver.common.by import By
import random, time

def create_paper(cfg, driver, base_url, exam_name, exam_time):
    driver.get(base_url + " ")
    driver.find_element_by_link_text(u"[登录]").click()
    driver.find_element_by_id("J_loginUsername").clear()
    driver.find_element_by_id("J_loginUsername").send_keys("haitian")
    driver.find_element_by_id("J_loginPassword").clear()
    driver.find_element_by_id("J_loginPassword").send_keys("1234")
    driver.find_element_by_css_selector("span.bluebtn35_text").click()
    #获得当前窗口句柄
    now_handle1 = driver.current_window_handle
    driver.find_element_by_link_text(u"考试系统").click()
    time.sleep(2)
    #获取所有窗口句柄
    all_handles1 = driver.window_handles 
    
    for handle1 in all_handles1:
        if handle1 != now_handle1:
            driver.switch_to_window(handle1)
            
    driver.find_element_by_xpath("//a[2]").click()
    now_handle = driver.current_window_handle #得到当前窗口句柄
    driver.find_element_by_link_text(u"新建试卷").click()
    time.sleep(2)
    all_handles = driver.window_handles #获取所有窗口句柄
    for handle in all_handles:
        if handle != now_handle:
            driver.switch_to_window(handle)
    driver.find_element_by_id("paper_name_input").clear()
    driver.find_element_by_id("paper_name_input").send_keys(exam_name)
    driver.find_element_by_id("exam_len").clear()
    driver.find_element_by_id("exam_len").send_keys(exam_time)
    driver.find_element_by_id("create_step_one").click()
    time.sleep(2)
    #添加大题
    auto_creatquestion(cfg,driver,3)
   
    #导入试题
    driver.find_element_by_id("import_q_btn").click()
    driver.find_element_by_css_selector("label.import-list-item.clearfix > input[type=\"checkbox\"]").click()
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    time.sleep(2)
    #生成试卷
    driver.find_element_by_id("bulid_paper_btn").click()
    time.sleep(2)
    
        
#创建大题1=单选题，2=多选题，3=是非题，4=填空题，5=问答题，6=完型填空题，7=综合题       
def add_big_question_falsequestions(cfg, driver,qscore):
    driver.find_element_by_id("add_big_btn").click()
    driver.find_element_by_css_selector("span.cc-arrow").click()
    driver.find_element_by_xpath("//div[10]/ul/li[1]").click()
    #driver.find_element_by_id("add_q_description_input").clear()
    #driver.find_element_by_id("add_q_description_input").send_keys(u"是非题")
    driver.find_element_by_id("add_q_score_input").clear()
    driver.find_element_by_id("add_q_score_input").send_keys(qscore)
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    time.sleep(2)
    
    
    
#自动创建大题
def auto_creatquestion(cfg,driver,q_num):
    #prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    for i in range(q_num):
        qscore = '3'
        add_big_question_falsequestions(cfg, driver, qscore)
        print i
 
    
#自动创建试卷
def auto_createpaper(cfg,driver,base_url,exam_num):
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    for i in range(exam_num):
        exam_name = 'testpaper_' + prefix + str(i) 
        exam_time = '120'
        qscore = '3'
        create_paper(cfg, driver, base_url, exam_name, exam_time)
        print i
      

def exam_result(cfg, driver, base_url, exam_name, etype=3, username=""):
    """
    etype表示需要的操作类型，1为导出分发给学员的试卷统计结果，
                             2为导出作为开放试卷的统计结果, 
                             3代表为学员评分
    """
    #exam_name = u"未作答（主观题，免费）"
    username = "sunmin1990"
    driver.get("%sexam/" %(base_url))
    driver.find_element_by_link_text(u"试卷库").click()
    driver.find_element("id", "search_text").send_keys(exam_name)
    time.sleep(1)
    exam_href = driver.execute_script("return $(\"a:contains(\'"+exam_name+"\')\").attr('href')")
    driver.get("%sexam/%s" % (base_url, exam_href))
    driver.find_element_by_link_text("学员信息").click()
    if etype == 2:
        driver.find_element_by_link_text(u"作为开放试卷的统计结果").click()
        driver.find_element("id", "select_all_btn").click()
        driver.find_element("id", "output_btn_open").click()
        time.sleep(2)
    elif etype == 1:
        driver.find_element("id", "select_all_btn").click()
        driver.find_element("id", "output_btn").click()
    else:
        #取评分链接
        time.sleep(1)
        grade_href = driver.execute_script("return $(\"a:contains(\'"+username+"\')\").parents('.odd').children().eq(5).children().attr('href')")
        driver.get("%sexam/%s" % (base_url, grade_href))
        score_input = driver.find_elements("class name", "subjective-score-input")
        for item in score_input:
            item.clear()
            item.send_keys("0.1")
        driver.find_element("id", "sava_btn").click()
 
    time.sleep(5)

def exam_grade(cfg, driver, base_url, exam_name, username):
    driver.fin

    
    
    
        