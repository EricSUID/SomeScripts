"""
功能：链滴(原黑客派)自动签到脚本
配置：社区登录账号 + 密码
"""

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

username = '请输入自己的账号'  # 账号
password = '请输入自己的密码'  # 密码
login_url = 'https://hacpai.com/login?goto=https%3A%2F%2Fhacpai.com%2F'  # 登录URL
checkin_url = 'https://hacpai.com/activity/checkin'  # 签到URL

driver = webdriver.Chrome()  # 初始化chrome
driver.maximize_window()  # 最大化窗口
driver.get(login_url)  # 进入登录页面

try:
    # driver.find_element_by_xpath(
    #     "//*[@id='verifyHacpaiIcon' and @class='fn__flex verify__via icon-hacpai']").click()  # 使用社区账号登录
    # time.sleep(1)  # 延时加载
    driver.find_element_by_id('nameOrEmail').send_keys(username)  # 填充用户名
    driver.find_element_by_id('loginPassword').send_keys(password)  # 填充密码
    driver.find_element_by_id('loginBtn').click()  # 登录
    time.sleep(1.5)
    driver.get(checkin_url)
    try:  # 未签到
        driver.find_element_by_xpath("//*[@class='btn green']").click()  # 签到
        print("签到成功")
    except NoSuchElementException:
        print("已签到")
except Exception as e:
    print(e)
    print("签到失败")

driver.quit()
