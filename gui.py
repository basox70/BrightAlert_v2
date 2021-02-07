import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get("file:///C:/Users/Zakaria%20Abdisalam/Desktop/Homepage%20-%20Universit%C3%A9%20d'Ottawa%20_%20University%20of%20Ottawa.html")

time.sleep(4)

coords = pyautogui.locateOnScreen('scan.png')
pyautogui.screenshot('img/scan1.png', region = coords)
# driver.close()
