from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pyautogui
from pyautogui import ImageNotFoundException
import PIL
import time

JUMP_TIMING = 232  # pixel X coordinate of screenshot
JUMP_BREAK = 0  # sleep time after jumping

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
    im = pyautogui.screenshot(imageFilename='my_screenshot.png ', region=(start_x, start_y, 400, 110))

while robot_rex:
    image = pyautogui.screenshot(region=(start_x, start_y, 400, 150))
    mode = image.getpixel((1, 109))

    for cor in range((JUMP_TIMING - 30), (JUMP_TIMING + 25), 4):
        # cactus and low bird detection
        pixel = image.getpixel((cor, 60))
        if mode[0] > 100 > pixel[0] or mode[0] < 100 < pixel[0]:
            pyautogui.press('space')
            time.sleep(JUMP_BREAK)
            break
        # middle bird detection
        pixel = image.getpixel((cor + 40, 40))
        if mode[0] > 100 > pixel[0] or mode[0] < 100 < pixel[0]:
            pyautogui.press('space')
            time.sleep(JUMP_BREAK)
            break

# it jumps again after middle bird, why?
# does break loop mean the for loops start again or is it just going out of the if statement? should i use continue instead???