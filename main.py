from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pyautogui
from pyautogui import ImageNotFoundException
import PIL
import time

JUMP_TIMING = 230

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
    im = pyautogui.screenshot(imageFilename='my_screenshot.png ', region=(start_x, start_y, 400, 100))

while robot_rex:
    image = pyautogui.screenshot(region=(start_x, start_y, 400, 100))
    mode = image.getpixel((1, 1))

    for cor in range((JUMP_TIMING - 40), (JUMP_TIMING + 40), 3):
        pixel = image.getpixel((cor, 60))
        if mode[0] > 100 > pixel[0] or mode[0] < 100 < pixel[0]:
            pyautogui.press('space')
            break
        pixel = image.getpixel((cor, 40))
        if mode[0] > 100 > pixel[0] or mode[0] < 100 < pixel[0]:
            pyautogui.press('space')
            break
