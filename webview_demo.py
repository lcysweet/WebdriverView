import time
from appium import webdriver

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = '.BrowserActivity'
# 不要重置应用
# desired_caps['noReset'] = True
# toast
# desired_caps['automationName'] = 'Uiautomator2'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 业务
# 开的手机/模拟器浏览器,输入rul,并按回车键66
driver.find_element_by_id("com.android.browser:id/url").send_keys("www.baidu.com")
time.sleep(1)
driver.press_keycode(66)
time.sleep(3)
print(driver.contexts)
# 告诉appium需要查找的是 com.android.browser程序的webview的内容
# 切换到网页去  重要(要填写的内容是:driver.contextx打印的第二个页面,第一个原生)
driver.switch_to.context("WEBVIEW_com.android.browser")
time.sleep(1)
print(driver.contexts)
# 网页的正式内容
# 1-百度输入框-输入内容
driver.find_element_by_id("index-kw").send_keys("10086")
time.sleep(3)
# 2- 点击 百度一下 按钮
driver.find_element_by_id("index-bn").click()
time.sleep(3)
# 切换到原生
driver.switch_to.context("NATIVE_APP")
driver.find_element_by_id("com.android.browser:id/url").send_keys("www.zhihu.com")
time.sleep(3)
driver.press_keycode(66)







# 结束
# time.sleep(2)
# driver.quit()
