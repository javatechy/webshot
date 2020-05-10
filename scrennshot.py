#coding=utf-8                                                                                                                                                                              
import time
import cv2 
import numpy as np
import utils.logger as logger
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.headless = False # Make it true if you don't want to open a browser and provide the creds
# driver = webdriver.Chrome(options=options)

class BColor:
    """
    BColor printable colors in terminal
    """

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Python3 code here creating class 
class ResultRow:  
    def __init__(self, index, url):
        self.index = index  
        self.url = url 
        self.imgPer = 0 
        self.txtPer = 0 

def openUrlAndTakeScreenshot(URL, timeout, screenshot_name):
    if screenshot_name.startswith('0'):
        timeout = timeout * 2     
    driver.maximize_window()
    driver.get(URL)
    time.sleep(timeout)
    driver.execute_script("document.body.style.zoom = 0.48") # reducing the window size by 50%
    time.sleep(2)
    driver.find_element_by_tag_name('body').screenshot(screenshot_name)
    

def compareImages(firstImage, secondImage):
    print("comparing  logic  : "+ firstImage + "  and second "+secondImage)
    image1 = cv2.imread(firstImage) 
    image2 = cv2.imread(secondImage) 
    print("started logic  : ")
    result = cv2.matchTemplate(image2, image1)
    print("started logic  : " + str(result))
    if image1.shape != image2.shape:
        return 0
    try:
        res = cv2.absdiff(image1, image2)
        res = res.astype(np.uint8)
        #--- find percentage difference based on number of pixels that are not zero ---
        percentage = 100 - ((np.count_nonzero(res) * 100)/ res.size)
        return percentage
    except Exception as e: # work on python 2.x
        logger.error('Noting is matching- Size has lot of difference'+ str(e))
        return -1
    '''
    print("Pecentage difference : ", percentage)
    difference = cv2.subtract(image1,image2)
    cv2.imshow("difference",difference)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

def execute(input_path, defaultTimePage):
    logger.log_r("Printing the entire list")
    # index =0
    # creating list        
    list = []
    index = 0
    with open(input_path, 'r') as f:
        for url in f:
            # openUrlAndTakeScreenshot(url, defaultTimePage, str(index) + '.png')
            list.append(ResultRow(index, url)) 
            logger.log_g(str(index))
            index = index+1
    
    logger.log_r("Printing the entire list")

    for obj in list: 
        percentage = compareImages('0.png', str(obj.index) + '.png')
        logger.log_g("percentage : " + str(percentage))
        obj.imgPer = percentage
        print(obj.index, obj.url, obj.imgPer, sep =' ' )

    print_results(list)
        
def print_results(results):
    results.sort(key=lambda x: x.imgPer)
    print(tabulate([[
        "  {color}{language}{end}".format(
            color=(BColor.BOLD if result.imgPer >0  else ""),
            language=str(result.index),
            end=BColor.ENDC),

        "  {color}{author}{end}  ".format(
            color=(BColor.BOLD if result.imgPer >0 else BColor.GREEN),
            author=result.url,
            end=BColor.ENDC),

        "  {color}{per:8.2f} %{end}".format(
            color=BColor.BOLD,
            per=result.imgPer,
            end=BColor.ENDC),

        "  {color}{answer}{end}  ".format(
            color=(BColor.BOLD if result.imgPer >0  else BColor.BLUE),
            answer=str(result.txtPer),
            end=BColor.ENDC,
        )
    ] for result in results], headers=["Serial Number","URL", "Image Match %", "Text Match %"]))

    