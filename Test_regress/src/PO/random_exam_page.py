'''
Created on Dec 19, 2014

@author: liwen
'''
import time 
import base

class  RandomExamPage(base.Base):
    def __init__(self, driver, cfg):
        self.cfg = cfg
        self.base_url = cfg.get('env_para', 'base_url')
        self.dr = driver 
        
    def click_random_btn(self):
        new_href = self.dr.execute_script("return $('.exam-random-btn').attr('href')")
        time.sleep(2)    
        self.dr.get("%sexam/%s" %(self.base_url,new_href))   
