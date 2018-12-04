from selenium import webdriver
b = webdriver.Firefox()
b.get('file:///Users/linning/Desktop/1.html')
ele = b.find_element_by_xpath('//input[1]')
ele.clear(),ele.send_keys('1111')
ele2 = b.find_element_by_xpath('//input[2]')
ele2.clear(),ele2.send_keys('2222')
print(ele.get_attribute('name'))
print(ele2.get_attribute('name'))
b.close()




