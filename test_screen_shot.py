#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''


from selenium.webdriver import Chrome

# with Chrome() as driver:
#     driver.get('http://www.baidu.com')
#     ele = driver.find_elements_by_css_selector('[title="点击一下，了解更多"]')
#     ele.screenshot('./image.png')
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
def test_dd():
    # from selenium import webdriver
    # from selenium.webdriver.chrome.options import Options
    # driver =webdriver.Chrome()

    from selenium import webdriver
    driver = webdriver.Chrome()

    # Navigate to url
    driver.get("http://www.google.com")

    # Store 'google search' button web element
    searchBtn = driver.find_element(By.LINK_TEXT, "Sign in")

    # Perform double-click action on the element
    webdriver.ActionChains(driver).double_click(searchBtn).perform()
