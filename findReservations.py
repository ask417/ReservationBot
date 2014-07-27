from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://facebook.com/')
browser.find_element_by_xpath("//*[@id='email']").send_keys("email")
browser.find_element_by_xpath("//*[@id='pass']").send_keys("password")
browser.find_element_by_xpath("//*[@id='loginbutton']").click()
