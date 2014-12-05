# -*- coding: UTF-8 -*-
'''
Created on Nov. 17, 2014

@author: yilulu
'''
import random
import time

from selenium.common.exceptions import NoSuchElementException


class Base():


    def __init__(self, driver):

        self.dr = driver

    def rand_name(self):
        rand_name = chr(random.randint(97, 122)) \
        + chr(random.randint(97, 122)) + chr(random.randint(97, 122)) \
        + str(random.randint(1000, 9999))

        return rand_name

    def datatime_name(self):
        name = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        return name

    def is_element_present(self, how, what):
        try: self.dr.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def save_screenshot(self):
        filename = self.datatime_name() + '.png'
        self.dr.save_screenshot(r"C://test_rs_pic//"+filename)

    def switch_window(self, bh):
        """
        bh是另弹出窗口前当前所有窗口句柄的列表
        bh = driver.window_handles
        """
        ah = self.dr.window_handles
        #有时间调用该转换窗口方法时，新窗口还没打开，所以需要判断下
        while len(bh) == len(ah):
            ah = self.dr.window_handles
        for h in ah:
            if h not in bh:
                self.dr.switch_to_window(h)