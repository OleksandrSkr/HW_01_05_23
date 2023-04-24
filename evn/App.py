#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#driver.get("https://www.google.com")

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.rozetka.com.ua")
time.sleep(15)
elem = driver.find_element(By.CSS_SELECTOR, ".search-form__input")
elem.send_keys('Samsung')

#elem = driver.find_element(By.CLASS_NAME, "search-form__input ng-pristine ng-valid ng-touched")
#/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div/input
#print(elem)
#print(elem.samsung)

#elem.send_keys("Samsung")
#class="search-form__input ng-pristine ng-valid ng-touched"
time.sleep(10)
