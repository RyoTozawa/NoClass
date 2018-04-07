#!/usr/bin/env python3
# coding:utf-8
from selenium import webdriver
from time import sleep
import Module.settings as settings
import Module.function as function

driver = webdriver.Firefox()
print('Start Driver')

target_url = settings.URL
driver.get(target_url)
sleep(1)
uid = driver.find_element_by_name('form1:htmlUserId')
password = driver.find_element_by_name('form1:htmlPassword')

user_id = settings.ID
user_password = settings.PASSWORD

uid.send_keys(user_id)
password.send_keys(user_password)
driver.find_element_by_name('form1:login').click()
print('Login Done')

out = []
try:
    current_window = driver.current_window_handle
    frame = driver.find_element_by_xpath("//*[contains(text(), '休講・補講情報')]").click()
    sleep(1)
    all_handles = driver.window_handles
    for handle in all_handles:
        if not(current_window == handle):
            driver.switch_to.window(handle)
            sleep(5)
            bodys = driver.find_element_by_xpath("//*[@class = 'mainTextScroll']")
            bodys = bodys.text.split('\n')
            no_class, extra_class = function.shape_string(bodys)
            if not(no_class is None) or not(extra_class is None):
                buffer = [no_class, extra_class]
                out.append(buffer)
except Exception as e:
    print(e)

sleep(5)
driver.close()
print(out)