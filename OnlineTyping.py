from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pyautogui
import time

driver = webdriver.Edge()
driver.get("https://onlinetyping.org")



#! Words are in id = "word-section" || class = "current-word"

#! Time is in id = "timer" || class = "type-btn" time is in min so change it to seconds for pyautogui

# r = requests.get("https://onlinetyping.org")
# time.sleep(3)

# soup = BeautifulSoup(r.text,"html.parser")
# with open("sample.html","w",encoding="utf-8") as f:
#     f.write(r.text)
# print(soup.prettify())


time.sleep(3)
elements = driver.find_elements(By.CLASS_NAME,"disrel")
print(elements)

time.sleep(3)
driver.close()