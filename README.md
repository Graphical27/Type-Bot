# TypeBot: Automated Typing Bot 

## 🤖 Project Description
TypeBot is an automated typing bot designed to interact with MonkeyType, a popular online typing test website. It uses Selenium WebDriver and PyAutoGUI to navigate the website, accept cookies, select typing mode, and automatically type the displayed text.

## 🖥️ Features
- Automatically opens MonkeyType.com
- Handles cookie consent banner
- Selects "words" typing mode
- Extracts text to type
- Simulates instant typing

## 🛠️ Prerequisites
Before running the script, ensure you have the following installed:

### 1. Python
- Python 3.7 or higher recommended
- Ensure Python is added to system PATH

### 2. Required Libraries
Install the following Python libraries using pip:
```bash
pip install selenium pyautogui
```

### 3. WebDriver Setup
#### Microsoft Edge WebDriver
1. Download Microsoft Edge WebDriver
   - Match the version with your installed Microsoft Edge browser
   - Download from: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

2. WebDriver Installation Options:
   - **Option A**: Add WebDriver to system PATH
   - **Option B**: Specify WebDriver path in script
   ```python
   driver = webdriver.Edge(executable_path='/path/to/msedgedriver')
   ```

## 🚀 How It Works
1. Opens MonkeyType in Microsoft Edge
2. Accepts cookie consent banner
3. Selects "words" typing mode
4. Extracts text from the typing area
5. Automatically types the entire text using PyAutoGUI

## 🔧 Configuration
- Adjust `time.sleep()` durations if needed for slower internet connections
- Modify XPath or CSS selectors if website structure changes

## ⚠️ Legal and Ethical Note
This bot is for educational purposes. Using automated tools on typing test websites may violate their terms of service.

## 🖼️ Bot Demo
![TypeBot Demo](https://placeholder.com/350x200)


