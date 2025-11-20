from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# считываем x
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
answer = calc(x)

# поле для ответа
input_field = browser.find_element(By.ID, "answer")

# Скроллим страницу — ключевой момент
browser.execute_script("arguments[0].scrollIntoView(true);", input_field)

input_field.send_keys(answer)

# чекбокс
robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
robot_checkbox.click()

# радиокнопка
robot_radiobutton = browser.find_element(By.ID, "robotsRule")
robot_radiobutton.click()

# кнопка
submit_btn = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()

# ждём, ловим число
alert = browser.switch_to.alert
print(alert.text)
alert_value = alert.text.split()[-1]
alert.accept()

browser.quit()

print("Your code:", alert_value)