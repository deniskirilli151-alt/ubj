from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

# укажи путь к драйверу (если не добавлен в PATH)
service = Service("C:\\chromedriver\\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.get("https://google.com")

print(driver.title)
sleep(3)
driver.quit()