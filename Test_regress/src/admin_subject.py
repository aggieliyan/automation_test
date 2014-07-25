'''
Created on 2014-7-23

@author: guoyuling
'''


import unittest, time, re,random


    
def create_subject(cfg,driver, base_url,org_name,subject_name):
    driver.get(base_url + "/organizationAdminRedirect.do?action=toOrganizationOffice&organizationId=122")
    time.sleep(2)
    driver.get("%sexam/" %(base_url))
    time.sleep(2)
    driver.find_element_by_id(cfg.get('tes_subject','new_subject_id')).click()
    driver.find_element_by_id(cfg.get('tes_subject','sub_name')).clear()
    driver.find_element_by_id(cfg.get('tes_subject','sub_name')).send_keys(subject_name)
    time.sleep(3)
    driver.find_element_by_xpath(cfg.get('tes_subject','sub_ok_xpath')).click()
    time.sleep(1)

def auto_create_subject(cfg,driver,base_url,org_name,sub_num):
    prefix = chr(random.randint(97,122))+chr(random.randint(97,122))+chr(random.randint(97,122))
    subject_info = []
    for i in range(sub_num):
        subject_name = org_name[0] +"sub_" +prefix+str(i)
        create_subject(cfg,driver, base_url,org_name,subject_name)
        subject_info.append(subject_name)
    return subject_info