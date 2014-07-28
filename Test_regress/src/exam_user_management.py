# -*- coding: UTF-8 -*-
'''
Created on Jul 24, 2014

@author: yilulu
'''

import time

def buy_paper(cfg, driver, paper_url=""):
    paper_url = "http://www.gamma.ablesky.com/examRedirect.do?action=viewExamPaperInfo&examPaperId=6129"
    driver.get(paper_url)
    time.sleep(1)
    driver.find_element(cfg.get('exam', 'buy_paper_by'), cfg.get('exam', 'buy_paper')).click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.find_element(cfg.get('org_index', 'pay_ok_by'), cfg.get('org_index', 'pay_ok')).click()
    time.sleep(5)

#学员考试
def exam(cfg, driver, base_url, operation, blank_pager, question_answer):
    time.sleep(2)
    driver.get(base_url+"exam/")
    time.sleep(2) 
    driver.find_element_by_link_text(u"立即考试").click()
    time.sleep(2)
    exam_time = driver.execute_script("return parseInt($('.pre-exam-outer li').eq(0).text().substring(5,6))")
    time.sleep(2)
    driver.find_element_by_link_text(u"开始考试").click()
    time.sleep(2)
    question_title = driver.execute_script("return $('#J_classification a:eq(0)').text()")
    time.sleep(2)
    if blank_pager == 0:
        #单选 多选
        if question_title == u"单选题" or question_title == u"多选题":
            driver.find_element(cfg.get('exam','exam_selectque_by'),cfg.get('exam','exam_selectque')).click()
        #是非题
        elif question_title == u"是非题":
            driver.find_element(cfg.get('exam','exam_yesnoque_by'),cfg.get('exam','exam_yesnoque')).click()    
        #填空题
        elif question_title == u"填空题":
            driver.find_element(cfg.get('exam','exam_blankque_by'),cfg.get('exam','exam_blankque')).send_keys(question_answer)    
        #问答题  
        elif question_title == u"问答题":
            iframe_id = driver.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
            driver.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
            idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
            element.innerHTML =\'"+question_answer+"\';")
        #完形填空题
        elif question_title == u"完形填空题":
            try:
                driver.find_element(cfg.get('exam','exam_clozeque_by'),cfg.get('exam','exam_clozeque')).click()
            except:
                None
        #综合题
        elif question_title == u"综合题":
            #第一个是单选 or 多选
            time.sleep(2)
            try:
                if driver.find_element(cfg.get('exam','exam_all_selectque_by'),cfg.get('exam','exam_all_selectque')):
                    driver.find_element(cfg.get('exam','exam_all_selectque_by'),cfg.get('exam','exam_all_selectque')).click()
            except:
                None
            #是非
            try:
                if driver.find_element(cfg.get('exam','exam_all_yesque_by'),cfg.get('exam','exam_all_yesque')):
                    driver.find_element(cfg.get('exam','exam_all_yesque_by'),cfg.get('exam','exam_all_yesque')).click()
            except:
                None
            #填空
            try:
                if driver.find_element(cfg.get('exam','exam_all_blankque_by'),cfg.get('exam','exam_all_blankque')):
                    driver.find_element(cfg.get('exam','exam_all_blankque_by'),cfg.get('exam','exam_all_blankque')).send_keys(question_answer)
            except:  
                None
            #问答
            try:
                if driver.find_element(cfg.get('exam','exam_all_askque_by'),cfg.get('exam','exam_all_askque')):
                    iframe_id = driver.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
                    driver.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
                    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
                    element.innerHTML =\'"+question_answer+"\';")
            except:
                None
        ###综合题结束
    if operation == 0 :
        time.sleep(exam_time * 60 + 2)
    else: 
        time.sleep(exam_time * 60 + 2)
        driver.find_element(cfg.get('exam','exam_submit_by'),cfg.get('exam','exam_submit')).click()#提交
        time.sleep(2)
        driver.find_element(cfg.get('exam','exam_continue_by'),cfg.get('exam','exam_continue')).click()#弹窗-继续考试
        time.sleep(2)
        driver.find_element(cfg.get('exam','exam_submit_by'),cfg.get('exam','exam_submit')).click()#提交
        time.sleep(2)
        driver.find_element(cfg.get('exam','window_submit_by'),cfg.get('exam','window_submit')).click()#弹窗-提交
        time.sleep(2)  
    