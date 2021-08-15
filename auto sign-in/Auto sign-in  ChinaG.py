"""
功能：ChinaG(几鸡-学习助理)自动签到脚本
配置：登录账号 + 密码
"""

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from win10toast import ToastNotifier

toaster = ToastNotifier()

username = '请输入自己的账号'
password = '请输入自己的密码'
login_url = 'http://j01.best/signin'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(login_url)

try:
    driver.find_elements_by_xpath("//input[@class='el-input__inner']")[0].send_keys(username)
    driver.find_elements_by_xpath("//input[@class='el-input__inner']")[1].send_keys(password)
    driver.find_elements_by_xpath("//button[@class='el-button el-button--primary']")[0].click()
    time.sleep(1.5)
    driver.find_elements_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary ']")[0].click()
    time.sleep(5)

    driver.find_elements_by_xpath("//button[@class='el-dialog__headerbtn']")[4].click()

    try:
        driver.find_element_by_partial_link_text("签").click()
        
        # todo 第一次签到的提示

        # 已经签到的提示
        toaster.show_toast("学习助理",
                           driver.find_element_by_xpath("//div[@class='el-message-box__title']").text + "\n" 
                           + driver.find_element_by_xpath("//div[@class='el-message-box__message']/div").text,
                           icon_path=None,
                           duration=10,
                           threaded=True)

    except NoSuchElementException:
        print("找不到按钮")

except Exception as e:
    print(e)
    print("签到失败")
    toaster.show_toast("学习助理", "签到失败", icon_path=None, duration=10, threaded=True)

driver.quit()
