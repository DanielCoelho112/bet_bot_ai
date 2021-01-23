#/usr/bin/python3.6
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
import os
import pickle

#PATH="~/home/danielc11/BET/geckodriver"
from selenium.webdriver.firefox.options import Options
'''
option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
webdriver.Firefox(firefox_profile=profile)




#profile = webdriver.FirefoxProfile()

profile.set_preference("dom.disable_open_during_load", False)
'''
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_profile=fp)
fp.set_preference("privacy.popups.disable_from_plugins", 3)
driver.implicitly_wait(10)

#driver.get("https://apostas.placard.pt/home")
driver.get('https://apostas.placard.pt/inplay')
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
#print(driver.title)

time.sleep(10)
element = driver.find_element_by_xpath("//div[@class='ta-Button']")
driver.execute_script("arguments[0].style.visibility='hidden'", element)
element.click()

#print(driver.page_source)


#file1 = open("MyFile.txt","a")
#file1.write(str(driver.page_source))
#file1.close()


#btn_Nao = driver.find_element_by_class_name("ta-Button")
#print(btn_Nao.text)
#btn_Nao.clear()
#button = driver.find_element_by_name('alert')
#button.click()
#alert_obj = driver.switch_to.alert
#print(alert_obj.text())

time.sleep(200)
driver.quit()
