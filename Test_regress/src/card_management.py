# -*- coding: UTF-8 -*-
'''
Created on Jun 1, 2012

@author: yilulu
'''
import time
import exam_paper
import exam_user_management
from PO.org_card_page import OrgCardgroupListPage, OrgCardgroupInputPage, OrgBuyliscardPage, \
    OrgAddcardPage, OrgUselearncardPage, OrgAcademyFirstPage, OrgAddExamcardPage, OrguseExamcardPage
from PO.exam_subject_page import SubjectListPage
from PO.exam_paper_page import ExamInfoPage, QuestionInfoPage

#使用充值卡和充课卡
def use_prepaidorcate_card(cfg, driver, base_url, card_num, card_psw):
    ogusecard = OrgUselearncardPage(driver, cfg)
    ogusecard.open_uselearncard()
    ogusecard.input_cardnum(card_num)
    ogusecard.input_cardpwd(card_psw)
    ogusecard.save_screenshot() 
    ogusecard.click_usenow()   
    ogusecard.click_pconfirmagain()
    prepaid_num = ogusecard.get_pcardnum()
    return prepaid_num        
  
#使用补课卡
def use_course_card(cfg, driver, base_url, card_num, card_psw):
    ogusecard = OrgUselearncardPage(driver, cfg)
    ogusecard.open_uselearncard()
    ogusecard.input_cardnum(card_num)
    ogusecard.input_cardpwd(card_psw)
    ogusecard.save_screenshot()
    ogusecard.click_usenow()
    ogusecard.select_relatecourse()
    ogusecard.click_selected()
    ogusecard.save_screenshot()
    ogusecard.click_confirmselect()
    course_num = ogusecard.get_ccardnum()  
    return course_num    

#添加卡组-充值卡
def add_prepaid_cardgroup(cfg, driver, base_url, org_name, \
        group_name, group_price=300):
    ogmancardgroup = OrgCardgroupListPage(driver, cfg)
    ogmancardgroup.open()
    ogmancardgroup.click_addcardgroup()
    ogaddcardgroup = OrgCardgroupInputPage(driver, cfg)    
    ogaddcardgroup.input_groupname(group_name)
    ogaddcardgroup.input_prepaidprice(group_price)
    ogaddcardgroup.save_screenshot()
    ogaddcardgroup.click_addgroup()
    
#添加卡组-充课卡
def add_course_cardgroup(cfg, driver, base_url, org_name, group_name):
    ogmancardgroup = OrgCardgroupListPage(driver, cfg)
    ogmancardgroup.open()
    ogmancardgroup.click_addcardgroup()
    ogaddcardgroup = OrgCardgroupInputPage(driver, cfg)
    ogaddcardgroup.select_coursecard() 
    ogaddcardgroup.input_groupname(group_name)
    ogaddcardgroup.select_relatecourse()
    ogaddcardgroup.save_screenshot()
    ogaddcardgroup.click_select()
    ogaddcardgroup.save_screenshot()
    ogaddcardgroup.click_addgroup()

#添加卡组-补课卡 
def add_cate_cardgroup(cfg, driver, base_url, org_name, \
        group_name, group_price=500):
    ogmancardgroup = OrgCardgroupListPage(driver, cfg)
    ogmancardgroup.open()
    ogmancardgroup.click_addcardgroup()
    ogaddcardgroup = OrgCardgroupInputPage(driver, cfg)
    ogaddcardgroup.select_catecard()
    ogaddcardgroup.input_groupname(group_name)
    ogaddcardgroup.select_relatecate()
    ogaddcardgroup.save_screenshot()
    ogaddcardgroup.input_cateprice(group_price)
    ogaddcardgroup.save_screenshot() 
    ogaddcardgroup.click_addgroup()

 #购买试听卡
def buy_listen_card(cfg, driver, base_url):
    ogmancardgroup = OrgCardgroupListPage(driver, cfg)
    ogmancardgroup.open()
    ogmancardgroup.click_buyliscard()
    ogbuyliscard = OrgBuyliscardPage(driver, cfg)    
    ogbuyliscard.input_buyliscardcount()
    ogbuyliscard.save_screenshot()
    ogbuyliscard.click_confirmbuyliscard()
    ogbuyliscard.save_screenshot()    
    ogbuyliscard.click_confirmgivemoney()
    
#添加卡组-试听卡
def add_listen_cardgroup(cfg, driver, base_url, \
        org_name, group_name):
    ogmancardgroup = OrgCardgroupListPage(driver, cfg)
    ogmancardgroup.open()
    ogmancardgroup.click_addcardgroup()
    ogaddcardgroup = OrgCardgroupInputPage(driver, cfg)
    ogaddcardgroup.select_listencard()
    ogaddcardgroup.input_groupname(group_name)
    ogaddcardgroup.select_listencourse()
    ogaddcardgroup.save_screenshot() 
    ogaddcardgroup.click_select()
    ogaddcardgroup.save_screenshot()
    ogaddcardgroup.click_addgroup()

#添加卡
def add_card(cfg, driver, org_name, base_url, \
        card_prifix,cgroup_num=1,card_num=5):
    ogmancardgroup = OrgCardgroupListPage(driver, cfg)
    ogmancardgroup.open()
    ogmancardgroup.click_addcard(cgroup_num)
    ogaddcard = OrgAddcardPage(driver, cfg)
    ogaddcard.input_cardprefix(card_prifix)    
    ogaddcard.input_cardnum(card_num)
    ogaddcard.save_screenshot() 
    ogaddcard.click_add()   
             
#机构获取院校机构类目名称
def get_academy_catename(cfg, driver, academy):
    ogacafpage = OrgAcademyFirstPage(driver, cfg)
    ogacafpage.open_academyfirstpage(academy)
    ogacafpage.save_screenshot()
    ogacafpage.click_selectcourse()       
    try:
        ogacafpage.click_closewindow() 
    except:
        ogacafpage.click_skip() 
        ogacafpage.click_selectcourse()
    finally:
        academy_catename = ogacafpage.get_firstcoursename()
        ogacafpage.save_screenshot()
        return academy_catename
    
#创建考试卡获取第一个考号
def add_exam_card_management(cfg, driver, base_url, count, academy):
    ogadexcard = OrgAddExamcardPage(driver, cfg)
    ogadexcard.click_more()
    ogadexcard.click_distributexam()
    ogadexcard.input_orgname(academy)  
    ogadexcard.input_examcardnum(count)
    ogadexcard.save_screenshot() 
    ogadexcard.click_ok()
    ogadexcard.click_more()  
    ogadexcard.enter_viewexamcardnumpage()  
    examcard_number = ogadexcard.get_examcardnum()
    return examcard_number       

#总调用方法####################################
def add_exam_card(cfg, driver, base_url, count, academy):
    page_catename = get_academy_catename(cfg, driver, academy)   
    #exam_paper.create_paper(cfg, driver, base_url, page_catename, 1, 1, 1, 1)
    ogsublist = SubjectListPage(driver, cfg)
    ogsublist.open()
#    ogsublist.click_exampaper()
    ogexaminfo = ExamInfoPage(driver, cfg)
    ogexaminfo.create_paper()
    time.sleep(3)
    ogexaminfo.input_exam_name(page_catename)
    ogexaminfo.save_screenshot()
    time.sleep(3)
    ogexaminfo.click_next()
    time.sleep(2)
    ogqueinfo = QuestionInfoPage(driver, cfg)
    time.sleep(2)
    ogqueinfo.add_big_question(1,1)
    time.sleep(2)
    ogexaminfo.save_screenshot()
    ogqueinfo.click_submit_btn()
    examcard_number = add_exam_card_management(cfg, driver, base_url, count, academy)
    return examcard_number

def user_usexamcard_management(cfg, driver, base_url, examcard_num):
    ogacafpage = OrgAcademyFirstPage(driver, cfg)
    academy = "qqhru"
    ogacafpage.open_academyfirstpage(academy)
    ogacafpage.click_selectcourse() 
    academy_catename = ogacafpage.get_firstcoursename()
    ogacafpage.click_selectfirstcourse()
    ogacafpage.save_screenshot() 
    ogacafpage.click_enterclearncener() 
    ogacafpage.click_examonline()
    ogacafpage.save_screenshot() 
    oguseexcard = OrguseExamcardPage(driver, cfg)
    oguseexcard.input_examcard(examcard_num)        
    oguseexcard.click_startexam()
    oguseexcard.save_screenshot()     
    return academy_catename

def user_usexamcard(cfg, driver, base_url, examcard_num):  
    academy_catename = user_usexamcard_management(cfg, driver, base_url, examcard_num)
    time.sleep(2)
    message = driver.execute_script("return $('p.error').text()")
    time.sleep(2)
    print message
    if message == "":
    # blank_pager=1是交白卷 ；blank_pager=0 是做了一个题
        exam_user_management.exam_user(cfg, driver, base_url, operation=0, blank_pager=0, question_answer='123', paper_name=academy_catename)
        return academy_catename

##使用充值卡和充课卡
#def use_prepaid_card(cfg, driver, base_url, card_num, card_psw):
#    driver.get(base_url+"useCard.do?action=toStudyCard")
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'card_num_by'), \
#        cfg.get('use_card', 'card_num')).send_keys(card_num)
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('use_card', 'card_psw_by'), \
#        cfg.get('use_card', 'card_psw')).send_keys(card_psw)
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('use_card', 'card_ok_by'), \
#        cfg.get('use_card', 'card_ok')).click()
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'prepaid_ok_by'), \
#        cfg.get('use_card', 'prepaid_ok')).click()
#    time.sleep(2)
#    prepaid_num = driver.find_element(cfg.get('use_card', 'confirm_prepaid_num_by'), \
#        cfg.get('use_card', 'confirm_prepaid_num')).text
#    driver.implicitly_wait(30)
#    return prepaid_num
##使用补课卡
#def use_course_card(cfg, driver, base_url, card_num, card_psw):
#    driver.get(base_url+"useCard.do?action=toStudyCard")
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'card_num_by'), \
#        cfg.get('use_card', 'card_num')).send_keys(card_num)
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('use_card', 'card_psw_by'), \
#        cfg.get('use_card', 'card_psw')).send_keys(card_psw)
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'card_ok_by'), \
#        cfg.get('use_card', 'card_ok')).click()
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'course_check_1_by'), \
#        cfg.get('use_card', 'course_check_1')).click()
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'course_check_2_by'), \
#        cfg.get('use_card', 'course_check_2')).click()

#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'add_ok_by'), \
#        cfg.get('use_card', 'add_ok')).click()
#    time.sleep(5)
#    driver.find_element(cfg.get('use_card', 'course_ok_by'), \
#        cfg.get('use_card', 'course_ok')).click()
#    time.sleep(2)
#    course_num = driver.find_element(cfg.get('use_card', 'confirm_course_num_by'), \
#        cfg.get('use_card', 'confirm_course_num')).text
#    return course_num  
##添加卡组-充值卡
#def add_prepaid_cardgroup(cfg, driver, base_url, org_name, \
#        group_name, group_price=300):
#    time.sleep(1)
#    driver.get(base_url + "myOffice.do")
#    time.sleep(5)
#    driver.find_element_by_link_text(u"管理/卡组").click()
#    time.sleep(3)
#    driver.find_element_by_link_text(u"添加卡组").click()
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'grouptitle_by'), \
#        cfg.get('org_manage', 'grouptitle')).send_keys(group_name)
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('org_manage', 'prepaid_price_by'), \
#        cfg.get('org_manage', 'prepaid_price')).send_keys(group_price)
#    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
#    driver.implicitly_wait(30)
##添加卡组-充课卡
#def add_course_cardgroup(cfg, driver, base_url, org_name, group_name):
#    driver.get(base_url + "myOffice.do")
#    driver.implicitly_wait(30)
#    driver.find_element_by_link_text(u"管理/卡组").click()
#    time.sleep(2)
#    driver.find_element_by_link_text(u"添加卡组").click()
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'course_card_by'), \
#        cfg.get('org_manage', 'course_card')).click()#选择充课卡
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'grouptitle_by'), \
#        cfg.get('org_manage', 'grouptitle')).send_keys(group_name)
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'course_dismore_by'), \
#        cfg.get('org_manage', 'course_dismore')).click()
#    time.sleep(5)
#    driver.execute_script("$('input[type=checkbox]:eq(2)').click()")#选择未归类类目下的一个课程
#    time.sleep(2)
#    driver.execute_script("$(\".x-btn-text\").eq(0).click()")
#    time.sleep(2)
#    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
#    driver.implicitly_wait(30)
##添加卡组-补课卡 
#def add_cate_cardgroup(cfg, driver, base_url, org_name, \
#        group_name, group_price=500):
#    driver.get(base_url + "myOffice.do")
#    driver.implicitly_wait(30)
#    driver.find_element_by_link_text(u"管理/卡组").click()
#    time.sleep(2)
#    driver.find_element_by_link_text(u"添加卡组").click()
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'grouptitle_by'), \
#        cfg.get('org_manage', 'grouptitle')).send_keys(group_name)
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'cate_card_by'), \
#        cfg.get('org_manage', 'cate_card')).click()
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'cate_by'), \
#        cfg.get('org_manage', 'cate')).click()
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'cate_price_by'), \
#        cfg.get('org_manage', 'cate_price')).send_keys(group_price)
#    driver.implicitly_wait(30)
#    driver.execute_script("$(\".x-btn-text\").eq(2).click()")
#    driver.implicitly_wait(30)
# #购买试听卡
#def buy_listen_card(cfg, driver, base_url):
#    driver.get(base_url + "myOffice.do")
#    driver.implicitly_wait(30)
#    driver.find_element_by_link_text(u"管理/卡组").click()
#    time.sleep(2)
#    driver.find_element_by_link_text(u"购买试听卡").click()
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'listen_count_by'), \
#        cfg.get('org_manage', 'listen_count')).send_keys('1')
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('org_manage', 'listen_buttion_by'), \
#        cfg.get('org_manage', 'listen_buttion')).click()
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('org_manage', 'listen_buttion_confirm_by'), \
#        cfg.get('org_manage', 'listen_buttion_confirm')).click()
#    time.sleep(2)
#    
##添加卡组-试听卡
#def add_listen_cardgroup(cfg, driver, base_url, \
#        org_name, group_name):
#    driver.get(base_url + "myOffice.do")
#    time.sleep(2)
#    driver.find_element_by_link_text(u"管理/卡组").click()
#    time.sleep(2)
#    driver.find_element_by_link_text(u"添加卡组").click()
#    time.sleep(3)
#    driver.find_element(cfg.get('org_manage', 'listen_card_by'), \
#        cfg.get('org_manage', 'listen_card')).click()#选择试听卡
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'grouptitle_by'), \
#        cfg.get('org_manage', 'grouptitle')).send_keys(group_name)
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'listen_spread_by'), \
#        cfg.get('org_manage', 'listen_spread')).click()#展开默认类目下资料
#    time.sleep(8)
#    driver.find_element(cfg.get('org_manage', 'listen_course_by'), \
#        cfg.get('org_manage', 'listen_course')).click()#勾选第一个课程
#    time.sleep(1)
#    try:
#        print driver.find_element(cfg.get('org_manage', 'listen_warn_by'), \
#        cfg.get('org_manage', 'listen_warn')).text
#    except:
#        None
#    time.sleep(1)
#    driver.execute_script("$(\".x-btn-text\").eq(0).click()")
#    time.sleep(1)
#    driver.execute_script("$(\".x-btn-text\").eq(2).click()")  
#    time.sleep(1)    
##添加卡
#def add_card(cfg, driver, base_url, org_name, \
#        card_prifix,cgroup_num=1,card_num=5):
#    driver.get(base_url + "myOffice.do")
#    time.sleep(2)
#    driver.find_element_by_link_text(u"管理/卡组").click()
#    time.sleep(2)
#    if cgroup_num == 1:
#        time.sleep(1)
#        driver.find_element_by_link_text(u"添加卡").click()
#    else:  
#        driver.find_element_by_xpath("//div["+str(cgroup_num)+ \
#            "]/table/tbody/tr/td[6]/div/div/a").click()
#    time.sleep(3)
#    try:
#        driver.find_element(cfg.get('org_manage', 'card_prefix_by'), \
#            cfg.get('org_manage', 'card_prefix')).send_keys(card_prifix)
#    except:
#        None
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'card_count_by'), \
#        cfg.get('org_manage', 'card_count')).send_keys(card_num)
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'add_card_ok_by'), \
#        cfg.get('org_manage', 'add_card_ok')).click()
#    time.sleep(2)
##机构获取院校机构类目名称
#def get_academy_catename(cfg, driver, base_url, academy):
#    driver.implicitly_wait(30)
#    driver.get(base_url + academy)
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'exam_selectcourse_by'), \
#        cfg.get('org_manage', 'exam_selectcourse')).click()#点击选课
#    try:
#        driver.find_element(cfg.get('org_manage', 'exam_select_close_by'), \
#            cfg.get('org_manage', 'exam_select_close'))#关闭窗口   
#    except:
#        time.sleep(2)
#        driver.find_element_by_link_text(u"跳过").click()#点击跳过
#        time.sleep(2)
#        driver.find_element(cfg.get('org_manage', 'exam_selectcourse_by'), \
#            cfg.get('org_manage', 'exam_selectcourse')).click()#点击选课
#    finally:
#        time.sleep(2)
#        academy_catename = driver.execute_script("return $(\'.wrap span\').eq(0).text()")#获取第一个课程名称
#        time.sleep(2)
#        return academy_catename
##创建考试卡获取第一个考号
#def add_exam_card_management(cfg, driver, base_url, count, academy):
#    time.sleep(2)
#    driver.execute_script("$('#paper_list_con a:eq(6)').click()")#点击更多
#    time.sleep(2)
#    driver.execute_script("$('#paper_list_con li:eq(0)').click()")#点击分配试卷  
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'exam_subname_by'), \
#        cfg.get('org_manage', 'exam_subname')).send_keys(academy)#添加机构名称 
#    driver.implicitly_wait(30)
#    driver.find_element(cfg.get('org_manage', 'exam_cardcount_by'), \
#        cfg.get('org_manage', 'exam_cardcount')).send_keys(count)#填写考试卡数量
#    time.sleep(2)
#    driver.find_element(cfg.get('org_manage', 'exam_ok_by'), \
#        cfg.get('org_manage', 'exam_ok')).click()#点击确定按钮
#    time.sleep(2)
#    driver.execute_script("$('#paper_list_con a:eq(6)').click()")#点击更多
#    time.sleep(2)
#    #获取点击查看卡号触发的链接
#    lookcardnum_url = driver.execute_script("return $('#paper_list_con li:eq(1)').attr('data-url')")
#    time.sleep(2)
#    driver.get(lookcardnum_url)#定位查看卡号连接
#    time.sleep(2)
#    examcard_number = driver.execute_script("return $('.first-cell span:eq(1)').text()")
#    time.sleep(2)
#    return examcard_number
##总调用方法
#def add_exam_card(cfg, driver, base_url, count, academy):
#    driver.implicitly_wait(30)
#    page_catename = get_academy_catename(cfg, driver, base_url, academy)
#    driver.implicitly_wait(30)
##    driver.get(base_url + "exam/")#考试系统链接     
##    time.sleep(3)
##    driver.find_element(cfg.get('org_manage', 'exam_list_by'), \
##        cfg.get('org_manage', 'exam_list')).click()#点击试卷库
##    time.sleep(3)
#    exam_paper.create_paper(cfg, driver, base_url, page_catename, 1, 1, 1, 1)
#    driver.implicitly_wait(30)    
#    examcard_number = add_exam_card_management(cfg, driver, base_url, count, academy)
#    return examcard_number
#def user_usexamcard_management(cfg, driver, base_url, examcard_num):
#    driver.implicitly_wait(30)
#    driver.get(base_url + "qqhru")
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'exam_selectcourse_by'), \
#        cfg.get('use_card', 'exam_selectcourse')).click()#点击选课
#    time.sleep(2)
#    academy_catename = driver.execute_script("return $(\'.wrap span\').eq(0).text()")#获取第一个课程名称
#    driver.execute_script("$('.wrap input').eq(0).click()")#选择第一个课程
#    time.sleep(2)
#    bh = driver.window_handles
#    driver.find_element(cfg.get('use_card', 'enter_study_center_by'), \
#        cfg.get('use_card', 'enter_study_center')).click()#将课程加入学习中心
#    time.sleep(2)
#    ah = driver.window_handles
#    while len(bh) == len(ah):
#        ah = driver.window_handles
#    for h in ah:
#        if h not in bh:
#            driver.switch_to_window(h)
#    time.sleep(2)
#    driver.get(base_url + "examRedirect.do?action=toUseExamCard")#获取点击线上考试
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'exam_inputnumber_by'), \
#        cfg.get('use_card', 'exam_inputnumber')).send_keys(examcard_num)#输入考号
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'exam_start_by'), \
#        cfg.get('use_card', 'exam_start')).click()#点击开始考试
#    time.sleep(2)
#    try:
#        print driver.execute_script("return $('p.error').text()")
#    except:
#        None
#    time.sleep(2)
#    driver.find_element(cfg.get('use_card', 'exam_paper_by'), \
#        cfg.get('use_card', 'exam_paper')).text#标题  
#    driver.implicitly_wait(30) 
#    return academy_catename
#def user_usexamcard(cfg, driver, base_url, examcard_num):  
#    academy_catename = user_usexamcard_management(cfg, driver, base_url, examcard_num)
#    # blank_pager=1是交白卷 ；blank_pager=0 是做了一个题
#    exam_user_management.exam_user(cfg, driver, base_url, operation=0, blank_pager=0, question_answer='123', paper_name=academy_catename)
