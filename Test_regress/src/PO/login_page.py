# -*- coding: UTF-8 -*-
'''
Created on Dec 9, 2014

@author: liwen
'''
import base, time


class  IndexPage(base.Base):
    
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver
        
    def open(self):
        url = "%sindex.do" %(self.base_url)
        self.dr.get(url)
        
class SearchPage(base.Base):
    
    def __init__(self,driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver  
        
    def open_search_page(self):
        url = "%sindex.do" %(self.base_url)
        self.dr.get('env_para', 'base_url') 

class IndependentDomianLoginPage(base.Base):
    def __init__(self,driver, cfg):
        self.cfg = cfg
        self.independent_url = cfg.get('env_para', 'independent_url')
        self.dr = driver  
        
    def open(self):
        url = self.independent_url
        self.dr.get(url)

class ClickLoginText(base.Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
    
    def click_login(self):
        time.sleep(3)
        try:
            self.dr.find_element_by_link_text(u"请登录").click()
        except:
            self.dr.find_element_by_link_text(u"登录").click()

    def click_register(self):
        time.sleep(3)
        try:
            self.dr.find_element_by_link_text(u"免费注册").click()
        except:
            self.dr.find_element_by_link_text(u"注册").click()
               
class LoginPage(base.Base):
    
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver
        
    def open_logindo(self):
        url = "%slogin.do" %(self.base_url)
        self.dr.get(url)
    
    def click_accounts(self):
        time.sleep(1)
        self.dr.find_element_by_class_name('login-switch').click()
                                
    def input_username(self,user_name):
        time.sleep(1)
        self.dr.find_element(self.cfg.get('search', 'login_username_by'), \
                        self.cfg.get('search', 'login_username')).send_keys(user_name)
    
    def input_pwd(self,user_psw):
        self.dr.find_element(self.cfg.get('search', 'login_psw_by'), \
                        self.cfg.get('search', 'login_psw')).send_keys(user_psw)
                        
    def click_login_btn(self):
        self.dr.find_element(self.cfg.get('login', 'login_btn_by'), \
                        self.cfg.get('login', 'login_btn')).click()
        
        

    
        