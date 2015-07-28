# -*- coding: UTF-8 -*-
'''
Created on Dec. 24, 2014
@author:liuhongjiao
modified on Dec. 24, 2014
@author: yanli
added import_questions
'''

import time
from selenium.webdriver.common.keys import Keys
from PO.exam_questions_page import QuestionListPage
from PO.exam_questions_page import QuestionInputPage

def import_questions(cfg, driver, template):
    questionlist = QuestionListPage(driver, cfg)
    questionlist.open()
    count = questionlist.click_import_questions(template)
    return count

    #创建单选题
def exam_question_single(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.add_music()
    question.input_answerab(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_questions(question_ansa)

    #创建多选题
def exam_question_multiple(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.click_question_type()
    question.click_question_multiple()
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.input_answerab(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_multiple()
    questionlist.search_questions(question_ansa)

    #创建是非题
def exam_question_trueorfalse(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.click_question_type()
    question.click_question_trueOrFalse()
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_trueorfalse()
    questionlist.search_questions(question_ansa)

    #创建问答题
def exam_question_answer(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.click_question_type()
    question.click_question_answer()
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.input_answer_answer(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_answer()
    questionlist.search_questions(question_ansa)

    #创建填空题
def exam_question_blank(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.click_question_type()
    question.click_question_blank()
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.input_blank_answer(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_blank()
    questionlist.search_questions(question_ansa)

    #创建完型填空题
def exam_question_cloze(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.click_question_type()
    question.click_question_cloze()
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.input_cloze_answer(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_cloze()
    questionlist.search_questions(question_ansa)

    #创建综合题
def exam_question_composite(cfg, driver, base_url, question_ansa):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    questionlist = QuestionListPage(driver, cfg)
    questionlist.click_question_create()
    question = QuestionInputPage(driver, cfg)
    question.click_question_type()
    question.click_question_composite()
    question.save_screenshot()
    question.input_question_name(question_ansa)
    question.input_composite_small_name(question_ansa)
    question.input_com_answerab(question_ansa)
    question.save_screenshot()
    question.click_question_save()
    questionlist.search_composite()
    questionlist.search_questions(question_ansa)

    #创建全部题型的试题
def auto_exam_questions(cfg, driver, base_url, question_ansa, num):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    #num为循环次数
    # 试题名称：
    # single:单选题
    # multiple：多选题
    # trueOrFalse：是非题
    # blank：填空题
    # answer：问答题
    # cloze：完型题
    # composite：综合题
    questionlist = QuestionListPage(driver, cfg)
    questionlist.open()
    questionlist.save_screenshot()
    for i in range(num):
        exam_question_single(cfg, driver, base_url, question_ansa)
        questionlist.save_screenshot()
        exam_question_multiple(cfg, driver, base_url, question_ansa)
        questionlist.save_screenshot()
        exam_question_trueorfalse(cfg, driver, base_url, question_ansa)
        questionlist.save_screenshot()
        exam_question_blank(cfg, driver, base_url, question_ansa)
        questionlist.save_screenshot()
        exam_question_answer(cfg, driver, base_url, question_ansa)
        questionlist.save_screenshot()
        exam_question_cloze(cfg, driver, base_url, question_ansa)
        questionlist.save_screenshot()
        exam_question_composite(cfg, driver, base_url, question_ansa)

    #创建一种题型的试题
def auto_exam_onequestion(cfg, driver, base_url, question_ansa, onetype):
    #question_ansa为创建试题时，题目和答案的内容，现在是用exam加随机数组成
    #onetype == 1:创建单选题
    #onetype == 2:创建多选题
    #onetype == 3:创建是非题
    #onetype == 4:创建填空题
    #onetype == 5:创建问答题
    #onetype == 6:创建完型题
    #onetype == 7:创建综合题
    questionlist = QuestionListPage(driver, cfg)
    questionlist.open()
    questionlist.save_screenshot()
    if onetype == 1:
        exam_question_single(cfg, driver, base_url, question_ansa)
    elif onetype == 2:
        exam_question_multiple(cfg, driver, base_url, question_ansa)
    elif onetype == 3:
        exam_question_trueorfalse(cfg, driver, base_url, question_ansa)
    elif onetype == 4:
        exam_question_blank(cfg, driver, base_url, question_ansa)
    elif onetype == 5:
        exam_question_answer(cfg, driver, base_url, question_ansa)
    elif onetype == 6:
        exam_question_cloze(cfg, driver, base_url, question_ansa)
    elif onetype == 7:
        exam_question_composite(cfg, driver, base_url, question_ansa)