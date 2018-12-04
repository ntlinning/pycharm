from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
b = webdriver.Firefox()
b.get('file:///Users/linning/Desktop/学习/jb51-1.net/%5BJava.Web.开发源码%5D.XML.XSLT.Servlet.JSP.深入剖析实例应用/JSPLesson/AppendixA/form.html')
ele = b.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input')
ele2 = b.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input')
ele3 = b.find_element_by_xpath('/html/body/form/table/tbody/tr[6]/td[2]/textarea')

ele4 = b.find_element_by_xpath('/html/body/form/table/tbody/tr[5]/td[2]/select')
ele5 = b.find_element_by_xpath('/html/body/form/table/tbody/tr[7]/td[2]/input')
ele.send_keys('linning')
ele2.send_keys('123456')
ele3.send_keys('1111')
ele4.send_keys('博士')
sleep(10)    #等待10毫秒
ele5.click()
sleep(10)
b.close()
