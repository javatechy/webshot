#coding=utf-8                                                                                                                                                                              
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.headless = False # Make it true if you don't want to open a browser and provide the creds
driver = webdriver.Chrome(options=options)

def openUrl(URL, timeout, screenshot_name):
    driver.maximize_window()
    driver.get(URL)
    time.sleep(timeout)
    driver.execute_script("document.body.style.zoom = 0.48") # reducing the window size by 50%
    driver.find_element_by_tag_name('body').screenshot(screenshot_name)
  
URL = 'https://microsoft.com'
openUrl(URL, 40, "spbootcamp.png")
openUrl('https://google.co.in', 20, "google.png")
driver.quit()