from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains #模拟用户行为
b = webdriver.Firefox()
b.get('https://www.waitsun.com')
b.maximize_window()   #最大化窗口
ele = b.find_elements_by_link_text('开发')
ActionChains(b).move_to_element(ele).perform()
ele2 = b.find_elements_by_link_text('思维导图')
ele2.click