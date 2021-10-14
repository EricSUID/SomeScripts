"""
功能：链滴(原黑客派)自动签到脚本
配置：社区登录账号 + 密码
"""

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from win10toast import ToastNotifier
import os
from datetime import datetime

toaster = ToastNotifier()

username = '请输入自己的账号'  # 账号
password = '请输入自己的密码'  # 密码
login_url = 'https://hacpai.com/login?goto=https%3A%2F%2Fhacpai.com%2F'  # 登录URL
checkin_url = 'https://hacpai.com/activity/checkin'  # 签到URL

driver = webdriver.Chrome()  # 初始化chrome
driver.maximize_window()  # 最大化窗口

try:
    driver.get(login_url)  # 进入登录页面

    try:
        driver.find_element_by_id('nameOrEmail').send_keys(username)  # 填充用户名
        driver.find_element_by_id('loginPassword').send_keys(password)  # 填充密码
        driver.find_element_by_id('loginBtn').click()  # 登录
        time.sleep(1.5)
        driver.get(checkin_url)
        try:
            driver.find_element_by_xpath("//*[@class='btn green']").click()  # 签到
            print("签到成功")
            toaster.show_toast("链滴", "签到成功", icon_path=None, duration=10, threaded=True)
        except NoSuchElementException:
            print("已签到")
            toaster.show_toast("链滴", "已经签过了", icon_path=None, duration=10, threaded=True)

    except Exception as e:
        print(e)
        print("签到失败")
        toaster.show_toast("链滴", "签到失败", icon_path=None, duration=10, threaded=True)

except Exception as e:
    print(e)
    print("访问失败")
    toaster.show_toast("链滴", "访问失败", icon_path=None, duration=10, threaded=True)

driver.quit()
