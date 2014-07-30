# -*- coding: UTF-8 -*-
'''
Created on Jul 23, 2014

@author: liwen
'''

from selenium.webdriver.common.by import By
import random, time

def create_paper(cfg, driver, base_url, exam_name, exam_time, eoperation, erandom, eopen):
    """
    operation 代表考试时间结束后操作 0代表默认值，自动交卷
                                 1代表 继续答题
    random 代表试题是否随机排序  0代表 否，不随机排序
                             1代表 是，随机排序
    eopen 代表试卷是否对外开放   0 代表否，不对外开放
                             1代表对外开放 
    """
    driver.get("%sexam/" %(base_url))
    time.sleep(1)
    driver.find_element(cfg.get('exam','exam_subject_by'),cfg.get('exam','exam_subject')).click()
    now_handle = driver.current_window_handle #得到当前窗口句柄
    driver.find_element_by_link_text(u"新建试卷").click()
    time.sleep(2)
    all_handles = driver.window_handles #获取所有窗口句柄
    for handle in all_handles:
        if handle != now_handle:
            driver.switch_to_window(handle)
    driver.find_element(cfg.get('exam','exam_paper_name_by'),cfg.get('exam','exam_paper_name')).clear()
    driver.find_element(cfg.get('exam','exam_paper_name_by'),cfg.get('exam','exam_paper_name')).send_keys(exam_name)
    driver.find_element(cfg.get('exam','exam_timelen_by'),cfg.get('exam','exam_timelen')).clear()
    driver.find_element(cfg.get('exam','exam_timelen_by'),cfg.get('exam','exam_timelen')).send_keys(exam_time)
    if eoperation == 0:
        driver.find_element(cfg.get('exam','exam_operation_auto_by'),cfg.get('exam','exam_operation_auto')).click()
    elif eoperation == 1:
        driver.find_element(cfg.get('exam','exam_operation_continue_by'),cfg.get('exam','exam_operation_continue')).click()
    if erandom == 0:
        driver.find_element(cfg.get('exam','exam_random_false_by'),cfg.get('exam','exam_random_false')).click()
    elif erandom == 1:
        driver.find_element(cfg.get('exam','exam_random_true_by'),cfg.get('exam','exam_random_true')).click()
    if eopen == 0:
        driver.find_element(cfg.get('exam','exam_open_false_by'),cfg.get('exam','exam_open_false')).click()
    elif eopen == 1:
        driver.find_element(cfg.get('exam','exam_open_true_by'),cfg.get('exam','exam_open_true')).click()
        driver.find_element(cfg.get('exam','exam_times_down_by'),cfg.get('exam','exam_times_down')).click()
        driver.find_element(cfg.get('exam','exam_times_by'),cfg.get('exam','exam_times')).click()
        driver.find_element(cfg.get('exam','exam_paper_price_by'),cfg.get('exam','exam_paper_price')).clear()
        driver.find_element(cfg.get('exam','exam_paper_price_by'),cfg.get('exam','exam_paper_price')).send_keys("10")
    driver.find_element(cfg.get('exam','exam_next_one_by'),cfg.get('exam','exam_next_one')).click()
    time.sleep(2)
    #添加大题
    auto_creatquestion(cfg,driver,3)
    #生成试卷
    driver.find_element(cfg.get('exam','exam_paper_build_btn_by'),cfg.get('exam','exam_paper_build_btn')).click()
    time.sleep(2)    
        
#添加大题        
def add_big_question(cfg, driver,qscore, qtype):
    """
    qtype表示大题类型，1=单选题，2=多选题，3=是非题，4=填空题，5=问答题，6=完型填空题，7=综合题
    """
    driver.find_element(cfg.get('exam','paper_add_big_question_by'),cfg.get('exam','paper_add_big_question')).click()    
    time.sleep(1)
    if qtype == 1:
        
        time.sleep(2)
        driver.find_element_by_css_selector("span.cc-arrow").click()
        driver.find_element('xpath','//div[10]/ul/li').click()
        #driver.find_element_by_css_selector("li.cc-item.selectedItem").click()
        driver.find_element(cfg.get('exam','exam_question_score_by'),cfg.get('exam','exam_question_score')).clear()
        driver.find_element(cfg.get('exam','exam_question_score_by'),cfg.get('exam','exam_question_score')).send_keys(qscore)
        driver.find_element(cfg.get('exam','exam_add_big_question_ok_by'),cfg.get('exam','exam_add_big_question_ok')).click()
        time.sleep(2)
    else:
        driver.find_element(cfg.get('exam','exam_topic_dropdown_by'),cfg.get('exam','exam_topic_dropdown')).click()
        if qtype == 2:
            driver.find_element(cfg.get('exam','exam_topic_multiple_by'),cfg.get('exam','exam_topic_multiple')).click()
        if qtype == 3:
            driver.find_element(cfg.get('exam','exam_topic_true_or_false_by'),cfg.get('exam','exam_topic_true_or_false')).click()
        if qtype == 4:
            driver.find_element(cfg.get('exam','exam_topic_fills_by'),cfg.get('exam','exam_topic_fills')).click()
        if qtype == 5:
            driver.find_element(cfg.get('exam','exam_topic_question_by'),cfg.get('exam','exam_topic_question')).click()
        if qtype == 6:
            driver.find_element(cfg.get('exam','exam_topic_cloze_by'),cfg.get('exam','exam_topic_cloze')).click()
        if qtype == 7:
            driver.find_element(cfg.get('exam','exam_topic_comprehensive_by'),cfg.get('exam','exam_topic_comprehensive')).click()
        driver.find_element(cfg.get('exam','exam_question_score_by'),cfg.get('exam','exam_question_score')).clear()
        driver.find_element(cfg.get('exam','exam_question_score_by'),cfg.get('exam','exam_question_score')).send_keys(qscore)
        driver.find_element(cfg.get('exam','exam_add_big_question_ok_by'),cfg.get('exam','exam_add_big_question_ok')).click()
        time.sleep(2)
    #导入试题
    driver.find_element(cfg.get('exam','paper_import_question_by'),cfg.get('exam','paper_import_question')).click()
    time.sleep(2)
    #勾选全部
    driver.find_element(cfg.get('exam','paper_selece_all_by'),cfg.get('exam','paper_selece_all')).click()
    #driver.find_element_by_css_selector("label.import-list-item.clearfix > input[type=\"checkbox\"]").click()
    driver.find_element(cfg.get('exam','exam_add_big_question_ok_by'),cfg.get('exam','exam_add_big_question_ok')).click()
    time.sleep(3)        
    
#自动添加题型
def auto_creatquestion(cfg,driver,q_num):
    type = [2,3,4,5,6,7]
    for i in range(q_num):
        qscore = '3'
        qtype=random.choice(type)
        add_big_question(cfg, driver, qscore, qtype)
        
#向试卷中导入试题        
def exam_export_question(cfg, driver,qscore, qtype):
    driver.find_element(cfg.get('exam','paper_import_question_by'),cfg.get('exam','paper_import_question')).click()
    time.sleep(2)
    #勾选全部
    driver.find_element(cfg.get('exam','paper_selece_all_by'),cfg.get('exam','paper_selece_all')).click()
    #driver.find_element_by_css_selector("label.import-list-item.clearfix > input[type=\"checkbox\"]").click()
    driver.find_element(cfg.get('exam','exam_add_question_ok_by'),cfg.get('exam','exam_add_question_ok')).click() 
    
#自动创建试卷
def auto_createpaper(cfg,driver,base_url,eoperation, erandom, eopen, exam_num):
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    for i in range(exam_num):
        exam_name = 'testpaper_' + prefix + str(i) 
        exam_time = '120'
        create_paper(cfg, driver, base_url, exam_name, exam_time,eoperation, erandom, eopen)
        print i
      

def exam_result(cfg, driver, base_url, exam_name, etype=1, username=""):
    """
    etype表示需要的操作类型，1为导出分发给学员的试卷统计结果，
                             2为导出作为开放试卷的统计结果,
                             3代表为学员评分
    """
    #exam_name = u"未作答（主观题，免费）"
    username = "sun123"
    driver.get("%sexam/" %(base_url))
    driver.find_element_by_link_text(u"试卷库").click()
    driver.find_element(cfg.get('exam', 'paper_search_by'), cfg.get('exam', 'paper_search')).send_keys(exam_name)
    time.sleep(1)
    exam_href = driver.execute_script("return $(\"a:contains(\'"+exam_name+"\')\").attr('href')")
    driver.get("%sexam/%s" % (base_url, exam_href))
    driver.find_element_by_link_text("学员信息").click()
    if etype == 2:
        driver.find_element_by_link_text(u"作为开放试卷的统计结果").click()
        time.sleep(1)
        driver.find_element(cfg.get('exam', 'select_paper_by'), cfg.get('exam', 'select_paper')).click()
        driver.find_element(cfg.get('exam', 'output_open_by'), cfg.get('exam', 'output_open')).click()
        
    elif etype == 1:
        driver.find_element(cfg.get('exam', 'select_paper_by'), cfg.get('exam', 'select_paper')).click()
        driver.find_element(cfg.get('exam', 'output_by'), cfg.get('exam', 'output')).click()
        a=driver.switch_to_alert()
        a.accept()
    else:
        #取评分链接
        time.sleep(5)
        grade_href = driver.execute_script("return $(\"a:contains(\'"+username+"\')\").parents('.odd').children().eq(5).children().attr('href')")
        time.sleep(5)
        driver.get("%sexam/%s" % (base_url, grade_href))
        time.sleep(2)
        score_input = driver.find_elements(cfg.get('exam', 'input_score_by'), cfg.get('exam', 'input_score'))
        score = "0.1"
        for item in score_input:
            item.clear()
            item.send_keys(score)
        driver.find_element(cfg.get('exam', 'score_save_by'), cfg.get('exam', 'score_save')).click()
        total_score = len(score_input) * score
        return total_score

    time.sleep(5)
    return True

def send_close_paper(cfg, driver, base_url, username="", atype=2):
    """
    参数atype为1表示为学员开通试卷，2表示为学员关闭试卷
    """
    username = "sunmin1990"
    driver.get("%sexam/" %(base_url))
    time.sleep(1)
    driver.find_element("xpath", "//p[4]/a").click()
    time.sleep(2)
    driver.find_element(cfg.get('exam', 'user_search_by'), cfg.get('exam', 'user_search')).clear()
    #driver.find_element(cfg.get('exam', 'user_search_by'), cfg.get('exam', 'user_search')).send_keys(username)
    #得一个字母一个字母的输入，否则因为输入太快得到的搜索结果不准确
    for letter in username:
        driver.find_element(cfg.get('exam', 'user_search_by'), cfg.get('exam', 'user_search')).send_keys(letter)
    time.sleep(1)
    if atype == 1:
        driver.find_element_by_link_text(u"分发试卷").click()
    else:
        driver.find_element_by_link_text(u"关闭试卷").click()
    time.sleep(1)
    driver.find_element(cfg.get('exam', 'open_paper_by'), cfg.get('exam', 'open_paper')).click()
    time.sleep(1)
    driver.find_element(cfg.get('exam', 'open_paper_ok_by'), cfg.get('exam', 'open_paper_ok')).click()
    time.sleep(5)
         