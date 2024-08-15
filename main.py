from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pyautogui
import PIL
import time

JUMP_BREAK = 0.2
JUMP_TIMING = 160

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
try:
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
except WebDriverException:
    time.sleep(2)

pyautogui.press('space')
time.sleep(1)

robot_rex = True
#TODO first locate where the dino is on the screen before narrowing down the screenshot area and the pixel comparer

im = pyautogui.screenshot(imageFilename='my_screenshot.png', region=(320,320, 400, 100))

while robot_rex:
    image = pyautogui.screenshot(region=(320,320, 400, 100))
    for cor in range((JUMP_TIMING - 40), (JUMP_TIMING + 30), 2):
        pixel = image.getpixel((cor, 60))
        if pixel[0] < 100:
            pyautogui.press('space')
            time.sleep(JUMP_BREAK)
            break
