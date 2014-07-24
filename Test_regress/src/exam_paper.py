# -*- coding: UTF-8 -*-
'''
Created on Jul 23, 2014

@author: liwen
'''

from selenium.webdriver.common.by import By
import random, time

def create_paper(cfg, driver, base_url, exam_name, exam_time):
    driver.get("%sexam/" %(base_url))
    time.sleep(1)
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
    #生成试卷
    driver.find_element_by_id("bulid_paper_btn").click()
    time.sleep(2)    
        
#添加大题        
def add_big_question(cfg, driver,qscore, qtype):
    """
    qtype表示大题类型，1=单选题，2=多选题，3=是非题，4=填空题，5=问答题，6=完型填空题，7=综合题
    """
    driver.find_element_by_id("add_big_btn").click()
    driver.find_element_by_css_selector("span.cc-arrow").click()
    if qtype == 1:
        driver.find_element_by_xpath("//div[10]/ul/li[1]").click()
    if qtype == 2:
        driver.find_element_by_xpath("//div[10]/ul/li[2]").click()
    if qtype == 3:
        driver.find_element_by_xpath("//div[10]/ul/li[3]").click()
    if qtype == 4:
        driver.find_element_by_xpath("//div[10]/ul/li[4]").click()
    if qtype == 5:
        driver.find_element_by_xpath("//div[10]/ul/li[5]").click()
    if qtype == 6:
        driver.find_element_by_xpath("//div[10]/ul/li[6]").click()
    if qtype == 7:
        driver.find_element_by_xpath("//div[10]/ul/li[7]").click()
    #driver.find_element_by_id("add_q_description_input").clear()
    #driver.find_element_by_id("add_q_description_input").send_keys(u"是非题")
    time.sleep(2)
    driver.find_element_by_id("add_q_score_input").clear()
    driver.find_element_by_id("add_q_score_input").send_keys(qscore)
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    time.sleep(2)
    #导入试题
    driver.find_element_by_id("import_q_btn").click()
    time.sleep(2)
    #勾选全部
    driver.find_element_by_id("select_all_btn").click()
    #driver.find_element_by_css_selector("label.import-list-item.clearfix > input[type=\"checkbox\"]").click()
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    time.sleep(3)        
    
#自动添加题型
def auto_creatquestion(cfg,driver,q_num):
    type = [1,2,3,4,5,6,7]
    for i in range(q_num):
        qscore = '3'
        qtype=random.choice(type)
        add_big_question(cfg, driver, qscore, qtype)
        
#向试卷中导入试题        
def exam_export_question(cfg, driver,qscore, qtype):
    driver.find_element_by_id("import_q_btn").click()
    driver.find_element_by_css_selector("label.import-list-item.clearfix > input[type=\"checkbox\"]").click()
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    time.sleep(2) 
    
#自动创建试卷
def auto_createpaper(cfg,driver,base_url,exam_num):
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    for i in range(exam_num):
        exam_name = 'testpaper_' + prefix + str(i) 
        exam_time = '120'
        create_paper(cfg, driver, base_url, exam_name, exam_time)
        print i
      

def export_exam_result(cfg, driver, base_url, exam_name, etype=1):
    """
    etype表示试卷类型，1为分发给学员的，2为作为开放试卷的
    """
    #exam_name = u"未作答（主观题，免费）"
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
    else:
        driver.find_element("id", "select_all_btn").click()
        driver.find_element("id", "output_btn").click()
 
    time.sleep(5)

    
    
    
        