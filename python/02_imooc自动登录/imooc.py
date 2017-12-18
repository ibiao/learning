
from selenium import webdriver
import time
# 打开浏览器
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# 打开网页
driver.get("https://www.imooc.com/")
time.sleep(1)
# 点击登录框
login = driver.find_element_by_id("js-signin-btn")
login.click()
time.sleep(1)
# 输入用户名
userName = driver.find_element_by_xpath('//*[@id="signup-form"]/div[1]/input')
userName.click()
userName.send_keys("chengshoubiao@163.com")
time.sleep(1)
# 输入密码
passWord = driver.find_element_by_xpath('//*[@id="signup-form"]/div[2]/input')
passWord.click()
passWord.send_keys("88888888888")
time.sleep(1)
# 登录
subbtn = driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]/input')
subbtn.click()

time.sleep(5)
driver.close()