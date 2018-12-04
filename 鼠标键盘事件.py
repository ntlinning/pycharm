from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains #模拟用户行为
driver = webdriver.Firefox()
driver.get('https://www.waitsun.com')
driver.maximize_window()   #最大化窗口
ele = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[5]/a')
ActionChains(driver).move_to_element(ele).perform()
sleep(5)
ele2 = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/ul/li[5]/ul/li[1]/a')
sleep(5)
ele2.click()
sleep(10)
driver.close()