# -*- coding: UTF-8 -*-
'''
Created on Jun 1, 2012

@author: yilulu
'''
import time

#使用充值卡和充课卡
def use_prepaid_card(cfg, driver, base_url, card_num, card_psw):
        
    driver.get(base_url+"useCard.do?action=toStudyCard")
    time.sleep(1)
    driver.find_element(cfg.get('use_card','card_num_id_by'),cfg.get('use_card','card_num_id')).send_keys(card_num)
    driver.find_element(cfg.get('use_card','card_psw_id_by'),cfg.get('use_card','card_psw_id')).send_keys(card_psw)
    driver.find_element(cfg.get('use_card','card_ok_css_by'),cfg.get('use_card','card_ok_css')).click()
    time.sleep(2)
    driver.find_element(cfg.get('use_card','prepaid_ok_css_by'),cfg.get('use_card','prepaid_ok_css')).click()
    time.sleep(2)
    
#使用补课卡
def use_course_card(cfg,driver, base_url, card_num, card_psw):
    
    driver.get(base_url+"useCard.do?action=toStudyCard")
    time.sleep(1)
    driver.find_element(cfg.get('use_card','card_num_id_by'),cfg.get('use_card','card_num_id')).send_keys(card_num)
    driver.find_element(cfg.get('use_card','card_psw_id_by'),cfg.get('use_card','card_psw_id')).send_keys(card_psw)
    driver.find_element(cfg.get('use_card','card_ok_css_by'),cfg.get('use_card','card_ok_css')).click()
    time.sleep(2)
    driver.find_element(cfg.get('use_card','course_check_1_name_by'),cfg.get('use_card','course_check_1_name')).click()
    driver.find_element(cfg.get('use_card','course_check_2_xpath_by'),cfg.get('use_card','course_check_2_xpath')).click()
    time.sleep(2)
    driver.find_element(cfg.get('use_card','add_ok_css_by'),cfg.get('use_card','add_ok_css')).click()
    time.sleep(2)
    driver.find_element(cfg.get('use_card','course_ok_css_by'),cfg.get('use_card','course_ok_css')).click()
    time.sleep(2)
  
#添加卡组-充值卡  
def add_prepaid_cardgroup(cfg, driver, base_url, org_name, group_name = u'prepaidcard100', group_price = 100):

    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"添加卡组").click()
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','grouptitle_id_by'),cfg.get('org_manage','grouptitle_id')).send_keys(group_name)
    driver.find_element(cfg.get('org_manage','prepaid_price_id_by'),cfg.get('org_manage','prepaid_price_id')).send_keys(group_price)
    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
    time.sleep(2)

#添加卡组-充课卡
def add_course_cardgroup(cfg,driver, base_url, org_name , group_name = u'coursecard'):
    
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"添加卡组").click()
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','course_card_xpath_by'),cfg.get('org_manage','course_card_xpath')).click()#选择充课卡
    driver.find_element(cfg.get('org_manage','grouptitle_id_by'),cfg.get('org_manage','grouptitle_id')).send_keys(group_name)
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','course_cate_xpath_by'),cfg.get('org_manage','course_cate_xpath')).click()#选择整个类目，类目下的课被选中
    #driver.find_element_by_css_selector("span.disMore_btn").click()
    #time.sleep(5)
    #driver.execute_script("$('input[type=checkbox]:eq(2)').click()")
    time.sleep(3)
    #driver.find_element_by_xpath(cfg.get('org_manage','course_ok_xpath')).click()
    driver.execute_script("$(\".x-btn-text\").eq(0).click()")
    time.sleep(3)
    driver.execute_script("$(\".x-btn-text\").eq(2).click()")

#添加卡组-补课卡 
def add_cate_cardgroup(cfg,driver, base_url, org_name,group_name = u'catecard-200', group_price = 200):
    
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    driver.find_element_by_link_text(u"添加卡组").click()
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','grouptitle_id_by'),cfg.get('org_manage','grouptitle_id')).send_keys(group_name)
    driver.find_element(cfg.get('org_manage','cate_card_xpath_by'),cfg.get('org_manage','cate_card_xpath')).click()
    time.sleep(3)
    driver.find_element(cfg.get('org_manage','cate_name_by'),cfg.get('org_manage','cate_name')).click()
    driver.find_element(cfg.get('org_manage','cate_price_id_by'),cfg.get('org_manage','cate_price_id')).send_keys(group_price)
    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
    time.sleep(2)
      

#添加卡
def add_card(cfg, driver, base_url, org_name, cgroup_num = 1,card_prifix='auto',card_num = 50):
     
    driver.get(base_url + "myOffice.do")
    time.sleep(2)
    driver.find_element_by_link_text(u"管理卡组").click()
    time.sleep(2)
    
    if cgroup_num == 1:
        driver.find_element_by_link_text(u"添加卡").click()
    else:  
        driver.find_element_by_xpath("//div["+str(cgroup_num)+"]/table/tbody/tr/td[6]/div/div/a").click()
    
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','card_prefix_id_by'),cfg.get('org_manage','card_prefix_id')).send_keys(card_prifix)
    time.sleep(3)
    driver.find_element(cfg.get('org_manage','card_count_id_by'),cfg.get('org_manage','card_count_id')).send_keys(card_num)
    time.sleep(3)
    driver.find_element(cfg.get('org_manage','add_card_ok_css_by'),cfg.get('org_manage','add_card_ok_css')).click()
    time.sleep(2)

#添加考试卡
def add_exam_card(cfg, driver, base_url,count = 5):
    time.sleep(2)
    driver.get(base_url + "qqhru")
    time.sleep(2)
    driver.find_element_by_link_text(u"跳过").click()#点击跳过
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_selectcourse_by'),cfg.get('org_manage','exam_selectcourse')).click()#点击选课
    time.sleep(2)
    coursename = driver.execute_script("return $(\'.wrap span\').eq(0).text()")#获取第一个课程名称
    time.sleep(2) 
    driver.find_element(cfg.get('org_manage','exam_select_close_by'),cfg.get('org_manage','exam_select_close')).click()#关闭窗口   
    time.sleep(2)
    driver.get(base_url + "exam/")#考试系统链接
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_list_by'),cfg.get('org_manage','exam_list')).click()#点击试卷库
    time.sleep(2)
    url_add = driver.execute_script("return $('.exam-common-action-con a').eq(0).attr('href')")#点击新建试卷的链接
    driver.get(base_url +'exam/'+url_add)
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_name_input_by'),cfg.get('org_manage','exam_name_input')).send_keys(coursename)
    time.sleep(2)
    driver.find_element_by_link_text(u"下一步").click()#点击下一步
    time.sleep(2)
    driver.find_element_by_link_text(u"添加题型").click()#点击下一步
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_confirm_by'),cfg.get('org_manage','exam_confirm')).click()#点击确定按钮
    driver.find_element_by_link_text(u"生成试卷").click()#点击生成试卷
    time.sleep(2)
    #driver.execute_script("$('#paper_list_con tr').eq(0).hover")#hover第一条
    time.sleep(2)
    driver.execute_script("$('#paper_list_con a:eq(6)').click()")#点击更多
    time.sleep(2)
    driver.execute_script("$('#paper_list_con li:eq(0)').click()")#点击分配试卷  
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_subname_by'),cfg.get('org_manage','exam_subname')).send_keys("qqhru")#添加机构名称 
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_cardcount_by'),cfg.get('org_manage','exam_cardcount')).send_keys(count)#填写考试卡数量
    time.sleep(2)
    driver.find_element(cfg.get('org_manage','exam_ok_by'),cfg.get('org_manage','exam_ok')).click()#点击确定按钮
    time.sleep(2)
    driver.execute_script("$('#paper_list_con a:eq(6)').click()")#点击更多
    lookcardnum_url = driver.execute_script("return $('#paper_list_con li:eq(1)').attr('data-url')")#获取点击查看卡号触发的链接
    time.sleep(2)
    driver.get(lookcardnum_url)#定位查看卡号连接
    time.sleep(2)
    examcard_number =driver.execute_script("return $('.first-cell span:eq(1)').text()")
    time.sleep(2)
    return examcard_number
def user_usexamcard(cfg, driver, base_url,examcard_num):
    time.sleep(2)
    driver.get(base_url + "qqhru")
    time.sleep(2)
    driver.find_element(cfg.get('use_card','exam_selectcourse_by'),cfg.get('use_card','exam_selectcourse')).click()#点击选课
    time.sleep(2)
    driver.execute_script("$('.wrap input').eq(0).click()")#选择第一个课程
    time.sleep(2)  
    driver.find_element(cfg.get('use_card','enter_study_center_by'),cfg.get('use_card','enter_study_center')).click()#将课程加入学习中心
    time.sleep(2)
    driver.get(base_url + "examRedirect.do?action=toUseExamCard")#获取点击线上考试
    time.sleep(2)
    driver.find_element(cfg.get('use_card','exam_inputnumber_by'),cfg.get('use_card','exam_inputnumber')).send_keys(examcard_num)#输入考号
    time.sleep(2)
    driver.find_element(cfg.get('use_card','exam_start_by'),cfg.get('use_card','exam_start')).click()#点击开始考试
    time.sleep(2)
    driver.find_element(cfg.get('use_card','exam_paper_by'),cfg.get('use_card','exam_paper')).text#标题  
    time.sleep(300)   
