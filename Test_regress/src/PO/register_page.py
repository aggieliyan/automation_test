'''
Created on Dec 9, 2014

@author: liwen
'''
import base

class AsRegisterPage(base.Base):
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver
                
class ClickRegisterText(base.Base):
    
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
    
    def click_register(self):
        self.dr.find_element_by_link_text(u"[注册]").click()
        
class RegisterPage(base.Base):
    def __init__(self, driver, cfg):
        self.dr = driver
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        
    def input_username(self,r_username):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_username_by'), \
                        self. cfg.get('as_index', 'register_email_username')).send_keys(r_username)
    
    def input_email(self,r_email):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_by'), \
                        self.cfg.get('as_index', 'register_email')).send_keys(r_email)
                        
    def input_phone(self,r_mobile):
        self.dr.find_element(self.cfg.get('as_index', 'register_mobile_number_by'), \
                        self.cfg.get('as_index', \
                                'register_mobile_number')).send_keys(r_mobile)
                        
    def input_pdw(self,r_psw):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_psw_by'), \
                        self.cfg.get('as_index', \
                                'register_email_psw')).send_keys(r_psw)
        self.dr.find_element(self.cfg.get('as_index', 'register_email_confirm_psw_by'), \
                        self.cfg.get('as_index', \
                                'register_email_confirm_psw')).send_keys(r_psw)
                                
    def verification_code(self):
        self.dr.find_elemen(self.cfg.get('as_index',"register_code_by"),\
                            self.cfg.get('as_index',"register_code")).click()
        self.dr.find_element(self.cfg.get('as_index',"register_code_by"),\
                            self.cfg.get('as_index',"register_code")).send_keys(raw_input(u"请输入验证码："))
                            
    def register_submit_btn(self):
        self.dr.find_element(self.cfg.get('as_index', 'register_email_submit_by'), \
                        self.cfg.get('as_index', 'register_email_submit')).click()
    
        
        
        
        
        
