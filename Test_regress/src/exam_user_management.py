# -*- coding: UTF-8 -*-
'''
Created on Jul 24, 2014

@author: yilulu
'''

import time

def buy_paper(cfg, driver, paper_url):
    #paper_url = "http://www.gamma.ablesky.com/examRedirect.do?action=viewExamPaperInfo&examPaperId=6129"
    driver.get(paper_url)
    time.sleep(1)
    driver.find_element(cfg.get('exam', 'buy_paper_by'), \
        cfg.get('exam', 'buy_paper')).click()
    h = driver.window_handles
    driver.switch_to_window(h[-1])
    driver.implicitly_wait(10)
    driver.find_element(cfg.get('org_index', 'pay_ok_by'), \
        cfg.get('org_index', 'pay_ok')).click()
    time.sleep(5)
#学员考试
def exam_user(cfg, driver, base_url, operation, blank_pager, question_answer, paper_name):
    driver.implicitly_wait(30)
    driver.get(base_url+"exam/")
    driver.implicitly_wait(30)
    items = driver.find_elements_by_css_selector(".exampaper-list-li")
    count = 0
    driver.implicitly_wait(30)
    for item in items:
        pager_name_get = driver.execute_script("return $('.exampaper-title').eq(" + str(count) + ").text()")
        if pager_name_get == unicode(paper_name):
            driver.implicitly_wait(30)
            url = driver.execute_script("return $('.exampaper-list-li a:eq(" + str(count) + ")').attr('href')")
            driver.get(base_url + "exam/" + url)#立即考试链接
        count += 1
    driver.implicitly_wait(30)
    exam_time = driver.execute_script("return parseInt($('.pre-exam-outer li').eq(0).text().substring(5,6))")
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"开始考试").click()
    time.sleep(2)
    question_title = driver.execute_script("return $('#J_classification a:eq(0)').text()")
    driver.implicitly_wait(30)
     # blank_pager=1 是白卷 ;blank_pager=0 是做了一个题
    if blank_pager == 0:
        #单选 多选
        if question_title == u"单选题" or question_title == u"多选题":
            try:
                driver.find_element(cfg.get('exam', 'exam_selectque_by'), \
                    cfg.get('exam', 'exam_selectque')).click()
            except:
                None     
        #是非题
        elif question_title == u"是非题":
            try: 
                driver.find_element(cfg.get('exam', 'exam_yesnoque_by'), \
                    cfg.get('exam', 'exam_yesnoque')).click()   
            except:
                None      
        #填空题
        elif question_title == u"填空题":
            try: 
                driver.find_element(cfg.get('exam', 'exam_blankque_by'), \
                    cfg.get('exam', 'exam_blankque')).send_keys(question_answer)   
            except:
                None  
        #问答题  
        elif question_title == u"问答题": 
            try:        
                 iframe_id = driver.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
                 driver.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
                 idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
                 element.innerHTML =\'"+question_answer+"\';")
            except:
                None 
        #完形填空题
        elif question_title == u"完形填空题":
            try:
                driver.find_element(cfg.get('exam', 'exam_clozeque_by'), \
                    cfg.get('exam', 'exam_clozeque')).click()
            except:
                None 
        #综合题
        elif question_title == u"综合题":
            #第一个是单选 or 多选
            driver.implicitly_wait(30)
            try:
                driver.find_element(cfg.get('exam', 'exam_all_selectque_by'), \
                    cfg.get('exam', 'exam_all_selectque')).click()
            except:
                None
            #是非
            try:
                driver.find_element(cfg.get('exam', 'exam_all_yesque_by'), \
                    cfg.get('exam', 'exam_all_yesque')).click()
            except:
                None
            #填空
            try:
                driver.find_element(cfg.get('exam', 'exam_all_blankque_by'), \
                    cfg.get('exam', 'exam_all_blankque')).send_keys(question_answer)
            except:  
                None
            #问答
            try:
                iframe_id = driver.execute_script("return $('#J_examWrapper iframe:eq(0)').attr('id')")
                driver.execute_script("var element=window.document.getElementById('" + iframe_id + "');\
                    idocument=element.contentDocument;element=idocument.getElementById('tinymce');\
                    element.innerHTML =\'"+question_answer+"\';")
            except:
                None
        ###综合题结束
        #等于0是自动提交
        if operation == 0:
             time.sleep(exam_time * 60 + 2)
        try:        
            driver.find_element(cfg.get('exam', 'exam_submit_by'), \
                cfg.get('exam', 'exam_submit')).click()#提交
            time.sleep(2)
            driver.find_element(cfg.get('exam', 'exam_continue_by'), \
                cfg.get('exam', 'exam_continue')).click()#弹窗-继续考试
            time.sleep(2)
            driver.find_element(cfg.get('exam', 'exam_submit_by'), \
                 cfg.get('exam', 'exam_submit')).click()#提交
            time.sleep(2)
            driver.find_element(cfg.get('exam', 'window_submit_by'), \
                cfg.get('exam', 'window_submit')).click()#弹窗-提交
            time.sleep(2) 
        except:
             None
    #学员提交白卷
    else:
        if operation == 0:
             time.sleep(exam_time * 60 + 2)
        try:   
            driver.find_element(cfg.get('exam', 'exam_submit_by'), \
                cfg.get('exam', 'exam_submit')).click()#提交
            time.sleep(2)
            driver.find_element(cfg.get('exam', 'exam_continue_by'), \
                cfg.get('exam', 'exam_continue')).click()#弹窗-继续考试
            time.sleep(2)
            driver.find_element(cfg.get('exam', 'exam_submit_by'), \
                cfg.get('exam', 'exam_submit')).click()#提交
            time.sleep(2) 
            driver.find_element(cfg.get('exam', 'window_submit_by'), \
                cfg.get('exam', 'window_submit')).click()#弹窗-提交
            time.sleep(2)  
        except:
             None