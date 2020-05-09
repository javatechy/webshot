# This will work using headless Chrome for any Desktop OS (Windows, MacOS, Linux Desktop)
from selenium import webdriver
import platform
import time

# Gets the path to the right chromedriver
path = "C:/webdrivers/chromedriver"

links = ['microsoft.sharepoint-df.com/teams/spbootcamp/_layouts/15/siteanalytics.aspx?view=19']

with webdriver.Chrome(path) as driver:
    for link in links:
        desktop = {'output': str(link) + '-desktop.png',
                   'width': 4588,
                   'height': 4588}
        tablet = {'output': str(link) + '-tablet.png',
                  'width': 1200,
                  'height': 1400}
        mobile = {'output': str(link) + '-mobile.png',
                  'width': 680,
                  'height': 1200}
        linkWithProtocol = 'https://' + str(link)

        # set the window size for desktop
        driver.set_window_size(desktop['width'], desktop['height'])
        driver.get(linkWithProtocol)
        time.sleep(50)
        el = driver.find_element_by_class_name('Files-mainColumn')
        total_height = ele.size["height"]+1000
        driver.set_window_size(1920, total_height)      #the trick
        time.sleep(2)
   
        el.screenshot("./divshot.png")

        # driver.save_screenshot(desktop['output'])

'''
        # set the window size for tablet
        driver.set_window_size(tablet['width'], tablet['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(tablet['output'])

        # set the window size for mobile
        driver.set_window_size(mobile['width'], mobile['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(mobile['output']) 
'''