#! python3

# 2048.py = Auto plays 2048
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# Sets the URL
url = "https://play2048.co/"

# Setting path for the Chrome Web Driver
PATH = "/usr/local/bin/chromedriver"

# Open the browser 
browser = webdriver.Chrome(PATH)
browser.get(url)
html = browser.find_element_by_tag_name('html')

while True:
    for h in range(15):
        for i in range(15):
            html.send_keys(Keys.RIGHT)
            html.send_keys(Keys.UP)
        html.send_keys(Keys.LEFT)
        html.send_keys(Keys.UP)
