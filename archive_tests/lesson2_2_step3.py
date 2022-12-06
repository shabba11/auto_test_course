from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    summ = int(x) + int(y)
    summ = str(summ)
    print(summ)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summ)
    
    browser.find_element(By.CLASS_NAME, "btn-default").click()
    




finally:
    time.sleep(30)
    browser.quit()