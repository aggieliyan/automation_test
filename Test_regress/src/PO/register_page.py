# -*- coding: UTF-8 -*-
'''
Created on Dec 9, 2014

@author: liwen
'''
import base, time
import selenium.common.exceptions

#class RegisterPage(base.Base):
#    def __init__(self, driver, cfg):
#        self.cfg = cfg
#        self.base_url = cfg.get('env_para', 'base_url')
#        self.dr = driver
#        
#    def open_index(self):
#        url = "%sindex.do" %(self.base_url)
#        self.dr.get(url)
#    
#    def open_login(self):
#        url = "%slogin.do" %(self.base_url)
#        self.dr.get(url)
                
class ClickRegisterText(base.Base):
    
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
    
    def click_register(self):
        self.dr.find_element_by_link_text(u"免费注册").click()
        
class EmailRegisterPage(base.Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        
    def click_emalimod(self):
        em = 0
        try:
            self.dr.find_element(self.cfg.get('as_index', 'register_email_type_by'), \
                                 self.cfg.get('as_index', 'register_email_type')).click()
        except Exception:
            print u"没有邮箱注册入口"
            em = 1
        return em
                                 
    def click_emailmod_domain(self):
        time.sleep(1)
        dem = 0
        try:
            self.dr.find_element(self.cfg.get('as_index', 'register_email_typedomain_by'), \
                                 self.cfg.get('as_index', 'register_email_typedomain')).click()
        except Exception:
            print u"没有邮箱注册入口"
            dem = 1
        return dem
                           
    def input_username(self,r_username):
        time.sleep(3)
        self.dr.find_element(self.cfg.get('as_index', 'register_email_username_by'), \
                        self. cfg.get('as_index', 'register_email_username')).send_keys(r_username)
    
    def input_email(self,r_email):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_by'), \
                        self.cfg.get('as_index', 'register_email')).send_keys(r_email)
                        
    def input_psw(self,r_psw):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_psw_by'), \
                        self.cfg.get('as_index', \
                                'register_email_psw')).send_keys(r_psw)
        self.dr.find_element(self.cfg.get('as_index', 'register_email_confirm_psw_by'), \
                        self.cfg.get('as_index', \
                                'register_email_confirm_psw')).send_keys(r_psw)
                                
    def verification_code(self):
        self.dr.find_element(self.cfg.get('as_index',"register_code_by"),\
                            self.cfg.get('as_index',"register_code")).click()
#        self.dr.find_element(self.cfg.get('as_index',"register_code_by"),\
#                            self.cfg.get('as_index',"register_code")).send_keys(raw_input(u"请输入验证码:"))
        time.sleep(5)                  
    def register_submit_btn(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_submit_by'), \
                        self.cfg.get('as_index', 'register_email_submit')).click()
                        
class PhoneRegisterPage(base.Base):
    
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        
    def input_username(self,r_username):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_username_by'), \
                        self.cfg.get('as_index', 'register_mobile_username')).send_keys(r_username)
    
    def input_mobile(self,r_mobile):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_number_by'), \
                        self.cfg.get('as_index', 'register_mobile_number')).clear()
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_number_by'), \
                        self.cfg.get('as_index', \
                                'register_mobile_number')).send_keys(r_mobile)
                        
    def input_psw(self,r_psw):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_psw_by'), \
                             self.cfg.get('as_index', 'register_mobile_psw')).clear()
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_psw_by'), \
                        self.cfg.get('as_index', 'register_mobile_psw')).send_keys(r_psw)
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_confirm_psw_by'), \
                        self.cfg.get('as_index', 'register_mobile_confirm_psw')).clear()
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_confirm_psw_by'), \
                        self.cfg.get('as_index','register_mobile_confirm_psw')).send_keys(r_psw)
                        
    def get_verification(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_getverify_by'), \
                        self.cfg.get('as_index', 'register_mobile_getverify')).click()
                                
    def verification_code(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_code_by'), \
                        self.cfg.get('as_index', 'register_mobile_code')).send_keys('')
                            
    def register_submit_btn(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_submit_by'), \
                        self.cfg.get('as_index', 'register_mobile_submit')).click()
                        
class IndependentAegisterPage(base.Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.independent_url = cfg.get('env_para', 'independent_url')
        
    def click_next(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_next_by'), \
                        self.cfg.get('as_index', 'register_email_next')).click()
                        
    def input_realname(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_realname_by'), \
                        self.cfg.get('as_index', 'register_email_realname')).clear()
        self.dr.find_element(self.cfg.get('as_index', 'register_email_realname_by'), \
                        self.cfg.get('as_index', \
                                'register_email_realname')).send_keys(u"真实姓名")
        
        
    
    
    
        
        
        
        
        
