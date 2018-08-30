# -*- coding: UTF-8 -*-
'''
Created on Aug 12, 2013

@author: yilulu
'''
import re
import time
from selenium.common.exceptions import NoSuchElementException

from PO.book_page import BookStepOnrPage,BookInfoPage,BookListPage
from PO.class_page import OnLineClassListPage, ClassInfoPage



#发布教辅图书
def new_book(cfg, driver, base_url, book_title=u'教辅图书',book_author='author',book_price='0.1',mark=0):

    book=BookStepOnrPage(driver,cfg)
    book.open()
    book.input_book_title(book_title)
    book.click_service_cate()
    book.click_next_step()
    time.sleep(1)

    book_info=BookInfoPage(driver,cfg)

    book_info.input_author(book_author)

    book_info.input_price(book_price)

    book_info.choose_if_mail(mark)
    time.sleep(1)
    book_info.click_save()
    time.sleep(2)

    #返回第一条图书数据，用来做断言
    bo = BookListPage(driver,cfg)
    bo.open_list()
    time.sleep(2)
    return bo.get_data()



#删除教辅图书
def del_book(cfg,driver):
    bo=BookListPage(driver,cfg)
    bo.open_list()
    data=bo.get_data()
    try:
        bo.click_del()
        return data
    except NoSuchElementException,e:
        print u'没有可删除教辅数据！'




