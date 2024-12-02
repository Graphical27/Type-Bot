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




flag = False
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_elements():
    print("Get called ================ ")
    global elements

    # Scroll the word-section into view
    word_section = driver.find_element(By.CSS_SELECTOR, "#word-section")
    driver.execute_script("arguments[0].scrollIntoView();", word_section)
    
    # Ensure all elements are visible and loaded
    elements = driver.find_elements(By.CSS_SELECTOR, "#word-section span")

    print(f"Found {len(elements)} span elements")  # Debug: number of span elements

    # Filter out empty strings
    words = [element.text for element in elements if element.text.strip()]

    print(words)  # Print collected words




time.sleep(3)
try:
    # Using button text or a partial attribute to identify the accept button
    accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Start Typing Test')]")
    accept_button.click()
    print("Typing test started")
    flag = True  # Use lowercase 'flag'
except Exception as e:
    print("Not Working")



if flag: 
    get_elements()


# print(elements)
time.sleep(100)
# driver.close()