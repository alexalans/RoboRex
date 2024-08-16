from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pyautogui
from pyautogui import ImageNotFoundException
import PIL
import time

#TODO reverse jump logic when screen goes black then white

JUMP_BREAK = 0.1
JUMP_TIMING = 185

robot_rex = True

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
except WebDriverException:
    time.sleep(2)

try:
    dinosaur = pyautogui.locateOnScreen('dinosaur.png')
except ImageNotFoundException:
    print("Dinosaur game not found. Make sure your internet connection is turned off")
    robot_rex = False
else:
    start_x = dinosaur[0]
    start_y = dinosaur[1]
    pyautogui.press('space')
    time.sleep(1)
    im = pyautogui.screenshot(imageFilename='my_screenshot.png', region=(start_x, start_y, 400, 100))

while robot_rex:
    image = pyautogui.screenshot(region=(start_x, start_y, 400, 100))
    for cor in range((JUMP_TIMING - 40), (JUMP_TIMING + 30), 3):
        pixel = image.getpixel((cor, 60))
        if pixel[0] < 100:
            pyautogui.press('space')
            time.sleep(JUMP_BREAK)
            break
        pixel = image.getpixel((cor, 40))
        if pixel[0] < 100:
            pyautogui.press('space')
            time.sleep(JUMP_BREAK)
            break
