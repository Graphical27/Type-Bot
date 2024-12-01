from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Edge()
driver.get("https://monkeytype.com")

# Wait for the page to load fully
time.sleep(3)

flag = False

try:
    # Using button text or a partial attribute to identify the accept button
    accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'accept')]")
    accept_button.click()
    print("Accepted cookies.")
    flag = True  # Use lowercase 'flag'
except Exception as e:
    print("Cookie accept button not found or already accepted.")

# After accepting cookies, click on the "words" button
if flag:
    try:
        words_button = driver.find_element(By.XPATH, "//button[@mode='words']")
        words_button.click()
        print("Clicked on the 'words' button.")
    except Exception as e:
        print("Error clicking the 'words' button:", e)
time.sleep(2)

Words = ""  # This will store the final string of words

# Function to extract elements text and format
def get_elements(elements):
    global Words  # Referencing global variable 'Words'
    for char in elements.text:
        if char == "\n":
            Words += " "  # Replace newline with space
        else:
            Words += char

# Function to simulate typing all the text at once using pyautogui
def type_bot():
    pyautogui.typewrite(Words, interval=0)  # Instant typing without delay
  # Type the whole string at once
    # time.sleep(0)  # No delay, type instantly

# Find the element that contains the text to type
elements = driver.find_element(By.CSS_SELECTOR, ".full-width.highlight-letter")

if flag:  # Only process if the cookie banner is accepted
    get_elements(elements)

type_bot()

time.sleep(100)
# driver.close()
