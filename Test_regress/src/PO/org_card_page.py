# -*- coding: UTF-8 -*-
'''
Created on Nov 17, 2014

@author: gaoyue
'''
import time
import base
from myoffice_page import MyOfficePage

class OrgCardgroupListPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def open(self):
		m = MyOfficePage(self.dr, self.cfg)
		m.open()
		m.click_org_operatage()
		m.click_org_mancardgroup()

	def click_addcardgroup(self):
		time.sleep(5)
		self.dr.find_element_by_link_text(u"添加卡组").click()
		
	def click_buyliscard(self):
		time.sleep(2)
		liscard = 0
		try:
			self.dr.find_element_by_link_text(u"购买试听卡").click()
		except:
			print u'机构为免费模式，没有试听卡购买入口'
			liscard = 1
		return liscard
		      
	def click_addcard(self, cgroup_num):
	    time.sleep(2)
	    if cgroup_num == 1:
		    time.sleep(1)
		    self.dr.find_element_by_link_text(u"添加卡").click()
	    else:  
		    self.dr.find_element_by_xpath("//div["+str(cgroup_num)+ \
			    "]/table/tbody/tr/td[6]/div/div/a").click()
		
class OrgCardgroupInputPage(base.Base):

	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def input_groupname(self, group_name):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'grouptitle_by'), \
		self.cfg.get('org_manage', 'grouptitle')).send_keys(group_name)

	def input_prepaidprice(self, group_price):
		self.dr.find_element(self.cfg.get('org_manage', 'prepaid_price_by'), \
		self.cfg.get('org_manage', 'prepaid_price')).send_keys(group_price)

	def click_addgroup(self):
		self.dr.execute_script("$(\".x-btn-text\").eq(2).click()")
		time.sleep(2)
	
	def select_coursecard(self):
		time.sleep(2)
		self.dr.find_elements(self.cfg.get('org_manage', 'course_card_by'), \
			self.cfg.get('org_manage', 'course_card'))[1].click()#选择充课卡
        
	def select_relatecourse(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'course_dismore_by'), \
			self.cfg.get('org_manage', 'course_dismore')).click()
		time.sleep(30)
		self.dr.execute_script("$('input[type=checkbox]:eq(2)').click()")#选择未归类类目下的一个课程
		time.sleep(2)

	def click_select(self):
		self.dr.execute_script("$(\".x-btn-text\").eq(0).click()")
		time.sleep(2)

	def select_catecard(self):
		time.sleep(2)
		self.dr.find_elements(self.cfg.get('org_manage', 'cate_card_by'), \
            self.cfg.get('org_manage', 'cate_card'))[2].click()

	def select_relatecate(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'cate_by'), \
            self.cfg.get('org_manage', 'cate')).click()

	def input_cateprice(self, group_price):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'cate_price_by'), \
            self.cfg.get('org_manage', 'cate_price')).send_keys(group_price)

	def select_listencard(self):
		time.sleep(2)
		self.dr.find_elements(self.cfg.get('org_manage', 'listen_card_by'), \
            self.cfg.get('org_manage', 'listen_card'))[-1].click()#选择试听卡
            
#	def select_listencourse(self):
#		time.sleep(2)
#		self.dr.find_element(self.cfg.get('org_manage', 'listen_spread_by'), \
#			self.cfg.get('org_manage', 'listen_spread')).click()#展开默认类目下资料
#		time.sleep(30)
#		self.dr.find_element(self.cfg.get('org_manage', 'listen_course_by'), \
#			self.cfg.get('org_manage', 'listen_course')).click()#勾选第一个课程
#		time.sleep(1)
#		try:
#			print self.dr.find_element(self.cfg.get('org_manage', 'listen_warn_by'), \
#			self.cfg.get('org_manage', 'listen_warn')).text
#		except:
#			None
#		time.sleep(1)
    #勾选免费课程
	def select_listencourse(self):
		time.sleep(2)
		self.dr.execute_script("$('.disMore_btn').eq(2).click()")#展开指定类目下资料
		time.sleep(30)
		self.dr.find_element(self.cfg.get('org_manage', 'listen_course_by'), \
			self.cfg.get('org_manage', 'listen_course')).click()#勾选第一个课程
		time.sleep(1)
		try:
			print self.dr.find_element(self.cfg.get('org_manage', 'listen_warn_by'), \
			self.cfg.get('org_manage', 'listen_warn')).text
		except:
			None
		time.sleep(1)

class OrgBuyliscardPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		
	def input_buyliscardcount(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('org_manage', 'listen_count_by'), \
            self.cfg.get('org_manage', 'listen_count')).send_keys('1')

	def click_confirmbuyliscard(self):
		self.dr.find_element_by_link_text(u"确认购买").click()
		
	def click_confirmgivemoney(self):
		self.dr.find_element(self.cfg.get('org_manage', 'listen_buttion_confirm_by'), \
            self.cfg.get('org_manage', 'listen_buttion_confirm')).click()
            
class OrgAddcardPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		
	def input_cardprefix(self, card_prifix):
	    time.sleep(3)
	    try:
		    self.dr.find_element(self.cfg.get('org_manage', 'card_prefix_by'), \
			    self.cfg.get('org_manage', 'card_prefix')).send_keys(card_prifix)
	    except:
		    None

	def input_cardnum(self, card_num):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('org_manage', 'card_count_by'), \
		    self.cfg.get('org_manage', 'card_count')).send_keys(card_num)
		
	def click_add(self):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('org_manage', 'add_card_ok_by'), \
		    self.cfg.get('org_manage', 'add_card_ok')).click()
	    time.sleep(1)
	    
class OrgUselearncardPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		
	def open_uselearncard(self):
	    self.dr.get(self.base_url+"useCard.do?action=toStudyCard")

	def input_cardnum(self, card_num):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('use_card', 'card_num_by'), \
		    self.cfg.get('use_card', 'card_num')).send_keys(card_num)

	def input_cardpwd(self, card_psw):
	    self.dr.find_element(self.cfg.get('use_card', 'card_psw_by'), \
		    self.cfg.get('use_card', 'card_psw')).send_keys(card_psw)
		    		
	def click_usenow(self):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('use_card', 'card_ok_by'), \
		    self.cfg.get('use_card', 'card_ok')).click()

	def click_pconfirmagain1(self):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('use_card', 'prepaid1_ok_by'), \
		    self.cfg.get('use_card', 'prepaid1_ok')).click()
		    
	def click_pconfirmagain(self):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('use_card', 'prepaid_ok_by'), \
		    self.cfg.get('use_card', 'prepaid_ok')).click()
		    
	def get_pcardnum(self):
	    time.sleep(2)
	    prepaid_num = self.dr.find_element(self.cfg.get('use_card', 'confirm_prepaid_num_by'), \
		    self.cfg.get('use_card', 'confirm_prepaid_num')).text
	    return prepaid_num
	   
	def select_relatecourse(self):
		time.sleep(5)
		self.dr.find_element(self.cfg.get('use_card', 'course_check_1_by'), \
			self.cfg.get('use_card', 'course_check_1')).click()
#		time.sleep(2)
#		self.dr.find_element(self.cfg.get('use_card', 'course_check_2_by'), \
#			self.cfg.get('use_card', 'course_check_2')).click()

	def click_selected(self):
		time.sleep(2)
		self.dr.find_element(self.cfg.get('use_card', 'add_ok_by'), \
			self.cfg.get('use_card', 'add_ok')).click()
		   
	def click_confirmselect(self):
		time.sleep(3)
		self.dr.find_element(self.cfg.get('use_card', 'course_ok_by'), \
			self.cfg.get('use_card', 'course_ok')).click()
					    
	def get_ccardnum(self):
		time.sleep(2)
		course_num = self.dr.find_element(self.cfg.get('use_card', 'confirm_course_num_by'), \
			self.cfg.get('use_card', 'confirm_course_num')).text
		return course_num
	
class OrgAcademyFirstPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')
		
	def open_academyfirstpage(self, academy):
	    self.dr.get(self.base_url+academy)

	def click_closewindow(self):
		self.dr.find_element(self.cfg.get('org_manage', 'exam_select_close_by'), \
			self.cfg.get('org_manage', 'exam_select_close'))#关闭窗口 
	
	def click_skip(self):
		time.sleep(2)
		self.dr.find_element_by_link_text(u"跳过").click()#点击跳过
		
	def click_selectcourse(self):
		time.sleep(3)
		self.dr.find_element(self.cfg.get('org_manage', 'exam_selectcourse_by'), \
			self.cfg.get('org_manage', 'exam_selectcourse')).click()#点击选课 
		
	def get_firstcoursename(self):
		time.sleep(2)
		academy_catename = self.dr.execute_script("return $(\'.wrap span\').eq(0).text()")#获取第一个课程名称
		time.sleep(2)
		return academy_catename
	
	def click_selectfirstcourse(self):
		time.sleep(1)
		self.dr.execute_script("$('.wrap input').eq(0).click()")#选择第一个课程
			
	def click_enterclearncener(self):
	    time.sleep(2)
	    bh = self.dr.window_handles
	    self.dr.find_element(self.cfg.get('use_card', 'enter_study_center_by'), \
		    self.cfg.get('use_card', 'enter_study_center')).click()#将课程加入学习中心
	    time.sleep(2)
	    ah = self.dr.window_handles
	    while len(bh) == len(ah):
		    ah = self.dr.window_handles
	    for h in ah:
		    if h not in bh:
			    self.dr.switch_to_window(h)
	 
	def click_examonline(self):
	    time.sleep(2)
	    self.dr.get(self.base_url + "examRedirect.do?action=toUseExamCard")#获取点击线上考试
			
class OrgAddExamcardPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def click_more(self):
	    time.sleep(2)
	    self.dr.execute_script("$('#paper_list_con a:eq(8)').click()")#点击更多 

	def click_distributexam(self):
	    time.sleep(2)
	    self.dr.execute_script("$('#paper_list_con li:eq(0)').click()")#点击分配试卷  
	    
	def input_orgname(self, academy):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('org_manage', 'exam_subname_by'), \
		    self.cfg.get('org_manage', 'exam_subname')).send_keys(academy)#添加机构名称 

	def input_examcardnum(self, count):
	    self.dr.find_element(self.cfg.get('org_manage', 'exam_cardcount_by'), \
		    self.cfg.get('org_manage', 'exam_cardcount')).send_keys(count)#填写考试卡数量
	    
	def click_ok(self):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('org_manage', 'exam_ok_by'), \
		    self.cfg.get('org_manage', 'exam_ok')).click()#点击确定按钮
	    
	def enter_viewexamcardnumpage(self):
	    time.sleep(2)
	    #获取点击查看卡号触发的链接
	    lookcardnum_url = self.dr.execute_script("return $('.more-ul li:eq(2)').attr('data-url')")
	    time.sleep(2)
	    self.dr.get(lookcardnum_url)#定位查看卡号连接
	    
	def get_examcardnum(self):
	    time.sleep(2)
	    examcard_number = self.dr.execute_script("return $('.first-cell span:eq(1)').text()")
	    time.sleep(2)
	    return examcard_number

class OrguseExamcardPage(base.Base):
	
	def __init__(self, driver, cfg):
		self.dr = driver
		self.cfg = cfg
		self.base_url = cfg.get('env_para', 'base_url')

	def input_examcard(self, examcard_num):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('use_card', 'exam_inputnumber_by'), \
		    self.cfg.get('use_card', 'exam_inputnumber')).send_keys(examcard_num)#输入考号 
		
	def click_startexam(self):
	    time.sleep(2)
	    self.dr.find_element(self.cfg.get('use_card', 'exam_start_by'), \
		    self.cfg.get('use_card', 'exam_start')).click()#点击开始考试
		

		 		   