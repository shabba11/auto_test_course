from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button1 = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotCheckbox")
    button1.click()

    button2 = browser.find_element(By.CSS_SELECTOR, ".form-check-input#robotsRule")
    button2.click()

    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.click()

finally:
    time.sleep(30)
    browser.quit()




