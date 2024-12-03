#=============================#==================================#======================================#====================#

#! Note: I tried from selenium and Bs4 but it didn't wokred + also tried to directly type the words and keep checking for new words tho didn't work so fro now I'm dropping bot for this site tho I have planned some ideas
                #* 1 : Planned to use image processing at runtime, Took screenshot everysecond and extract word from the pic tho it slow so not implement it 
                #* 2 : Download the whole webpage at once and then extract the words from it 

        #? If you have any diff plan feel free to implement it good luck


 #=============================#==================================#======================================#====================#


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import pyautogui
import time

driver = webdriver.Edge()
driver.get("https://onlinetyping.org")



#! Words are in id = "word-section" || class = "current-word"

#! Time is in id = "timer" || class = "type-btn" time is in min so change it to seconds for pyautogui

r = requests.get("https://onlinetyping.org")
# time.sleep(3)

# soup = BeautifulSoup(r.text,"html.parser")
# with open("sample.html","w",encoding="utf-8") as f:
#     f.write(r.text)
# print(soup.prettify())




flag = False
def get_elements():   # Didn't work 
    time.sleep(5)
    word_section = driver.find_element(By.ID, 'word-section')
    try:
        while True:
            print("working")
        # Simulate typing the word
            input_field = driver.switch_to.active_element
            input_field.send_keys(current_word)
            input_field.send_keys(Keys.SPACE)  # Press space after each word

            # Wait a short time to allow the next word to appear
            time.sleep(0.1)
            current_word = word_section.find_element(By.CLASS_NAME, 'current-word').text

    except Exception as e:
        print("Error occurred:", e)
    


# def get_elements():  # BS4 didn't work on it so gotta use selenium 
#     time.sleep(5) # wait the site to load
#     with open("sample.html", "w",encoding="utf-8") as f:
#         f.write(r.text)


time.sleep(3)  #! This working fine 
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