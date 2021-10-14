"""
功能：ChinaG(几鸡-学习助理)自动签到脚本
配置：登录账号 + 密码
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from win10toast import ToastNotifier
import os
from datetime import datetime

parent = os.getcwd() + "\\"

# print(parent)
file = open(parent + 'Auto_sign-in_ChinaG_Log' + '.txt', 'a')
file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
file.close()

toaster = ToastNotifier()

username = '请输入自己的账号'
password = '请输入自己的密码'
login_url = 'http://a.luxury/signin'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

try:
    driver.get(login_url)
    try:
        driver.find_elements_by_xpath("//input[@class='el-input__inner']")[0].send_keys(username)
        driver.find_elements_by_xpath("//input[@class='el-input__inner']")[1].send_keys(password)

        try:
            driver.find_elements_by_xpath("//button[@class='el-button el-button--primary']")[0].click()
            time.sleep(1.5)
            driver.find_elements_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary ']")[0].click()
            time.sleep(5)
            driver.find_elements_by_xpath("//button[@class='el-dialog__headerbtn']")[4].click()
            driver.find_element_by_partial_link_text("签").click()
            
            if driver.find_element_by_partial_link_text("签到流量"):
                driver.find_element_by_partial_link_text("签").click()

            time.sleep(1)
            if driver.find_element_by_partial_link_text("签"):
                driver.find_element_by_partial_link_text("签").click()
                toaster.show_toast("学习助理: 已签到",
                                   driver.find_element_by_xpath("//div[@class='el-message-box__title']").text + "\n"
                                   + driver.find_element_by_xpath("//div[@class='el-message-box__message']/div").text,
                                   icon_path=None,
                                   duration=10,
                                   threaded=True)

        except NoSuchElementException as e:
            driver.find_element_by_partial_link_text("签").click()
            toaster.show_toast("学习助理: 已签到",
                                driver.find_element_by_xpath("//div[@class='el-message-box__title']").text + "\n"
                                + driver.find_element_by_xpath("//div[@class='el-message-box__message']/div").text,
                                icon_path=None,
                                duration=10,
                                threaded=True)

    except Exception as e:
        print(e)
        print("签到失败")
        toaster.show_toast("学习助理", "签到失败", icon_path=None, duration=10, threaded=True)

except Exception as e:
    print(e)
    print("访问失败")
    toaster.show_toast("学习助理", "访问失败", icon_path=None, duration=10, threaded=True)

driver.quit()
