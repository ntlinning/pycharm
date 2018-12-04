from selenium import webdriver
b = webdriver.Firefox()
b.get('file:///Users/linning/Desktop/学习/jb51-1.net/%5BJava.Web.开发源码%5D.XML.XSLT.Servlet.JSP.深入剖析实例应用/JSPLesson/AppendixA/form.html')
ele = b.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[2]/input')




ele.send_keys('linning')