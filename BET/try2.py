#/usr/bin/python3.6
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
import os
import pickle
from selenium.webdriver.chrome.options import Options



#PATH="~/home/danielc11/BET/geckodriver"
from selenium.webdriver.chrome.options import Options



option=Options()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")


driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver",chrome_options=option)

#driver.get("https://apostas.placard.pt/home")
driver.get('https://apostas.placard.pt/inplay')

time.sleep(5)

try:
    aa=driver.find_element_by_css_selector('body > div:nth-child(23) > div > div.ta-Dialog > div > div.ta-Dialog-content > div > div > div:nth-child(2)')
    aa.click()
except:
    pass
#driver.find_element_by_xpath('<div class="ta-Button" style="position: relative; display: flex; box-sizing: border-box; flex: 1 1 auto; align-items: center; justify-content: center; border-radius: 2px; background-color: rgb(134, 188, 37); color: rgb(255, 255, 255); font-family: Panton; font-size: 14px; font-stretch: normal; font-weight: 700; text-decoration: none; text-transform: none; min-height: 40px; -webkit-tap-highlight-color: transparent; cursor: pointer; outline: none; margin: 0px 0px 0px 8px;">Sim</div>').click()
#try:

time.sleep(3)

try:
    bb=driver.find_element_by_css_selector('#app > div > header > div:nth-child(1) > div > div > div > div.ta-Button.ta-CookieConsentButton')
    bb.click()
except:
    pass
#except:
   # aa=driver.switch_to.active_element()

try:
    driver.find_element_by_css_selector('#app > div > header > div:nth-child(2) > div.ApplicationMenu > div > div:nth-child(2) > div > div.ta-Button.ta-loginButton').click()
except:
    pass

try:
    driver.find_element_by_css_selector('body > div:nth-child(22) > div > div.ta-Dialog > div > div.ta-ScrollPane > div > div > div > div:nth-child(1) > div > form > div:nth-child(1) > div:nth-child(1) > input').send_keys('DanielCoelho112')
    time.sleep(1)
    driver.find_element_by_css_selector('body > div:nth-child(22) > div > div.ta-Dialog > div > div.ta-ScrollPane > div > div > div > div:nth-child(1) > div > form > div:nth-child(1) > div:nth-child(3) > div.ta-PasswordInput > input').send_keys('zEBbgdi9cVtFGQ9')
    time.sleep(1)
    driver.find_element_by_css_selector('body > div:nth-child(22) > div > div.ta-Dialog > div > div.ta-ScrollPane > div > div > div > div:nth-child(1) > div > form > div.ta-FlexPane.ta-loginButton > div > input').click()
except:
    pass

time.sleep(10)

driver.find_element_by_css_selector('#app > div > main > div:nth-child(1) > div > div > div.ta-primary > div > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div > div:nth-child(1)').click()

time.sleep(5)


file1 = open("MyFile2.txt","a")
file1.write(str(driver.page_source))
file1.close()


driver.find_element_by_css_selector('#app > div > main > div:nth-child(1) > div > div > div.ta-primary > div > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(7) > div:nth-child(2) > div > div > div > div:nth-child(2) > div.ta-FlexPane > div:nth-child(1) > div > div:nth-child(1) > div').click()

time.sleep(3)
#driver.find_element_by_css_selector('#app > div > main > div.ta-FlexPane.ta-sideMenu > div.ta-FlexPane.ta-bettingCenterView > div > div:nth-child(2) > div > div > div > div.ta-ScrollPane > div.ta-FlexPane > div.ta-disabled-when-pending > div.Betslip-single_bets > div.singleBetContainer > div > div.ta-FlexPane > div:nth-child(2) > div > input').send_keys('1.00')

driver.find_element_by_css_selector('#app > div > main > div.ta-FlexPane.ta-sideMenu > div.ta-FlexPane.ta-bettingCenterView > div > div:nth-child(2) > div > div > div > div.ta-ScrollPane > div.ta-FlexPane > div.ta-disabled-when-pending > div.Betslip-single_bets > div.singleBetContainer > div > div.ta-FlexPane > div:nth-child(2) > div > input').send_keys('1')

time.sleep(3)

driver.find_element_by_css_selector('#app > div > main > div.ta-FlexPane.ta-sideMenu > div.ta-FlexPane.ta-bettingCenterView > div > div:nth-child(2) > div > div > div > div.ta-ScrollPane > div.ta-FlexPane > div.bet-placement-content > div:nth-child(1) > div.placebet-button-ACTIVE > div > input').click()


time.sleep(200)
driver.quit()
