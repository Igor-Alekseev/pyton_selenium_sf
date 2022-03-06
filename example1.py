

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("C:\Users\Игорь\projects\Skillfactory\pyton_selenium_sf\chromedriver")
driver.get("http://google.com")
driver.find_element(by.XPATH, "//input[@title=\"Поиск\"]").send_keys('Skillfactory' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
driver.quit()