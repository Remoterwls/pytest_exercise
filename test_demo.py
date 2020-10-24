#!usr/bin/env python
# encoding:utf-8
'''
__Author__: Jack Wu
__function__：
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo(object):

    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get('http://172.16.1.100:8080/ezaccur/managerPlatform')
        print(self.driver.title)
        print(self.driver.current_url)
        assert self.driver.current_url == 'http://172.16.1.100:8080/ezaccur/managerPlatform'
        sleep(3)

    def test_cookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        # self.driver.get('http://172.16.1.100:8080/ezaccur/threatPrecaution')
        # cookies = [{'domain': '172.16.1.100', 'expiry': 1603432497, 'httpOnly': False, 'name': 'EZACCUR', 'path': '/', 'secure': False, 'value': 'FC5593496F684496BFCCC3224A937579'},
        #            {'domain': '172.16.1.100', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/ezaccur', 'secure': False, 'value': 'FC5593496F684496BFCCC3224A937579'}]
        # # cookies = [{'domain': '172.16.1.100', 'expiry': 1603433554, 'httpOnly': False, 'name': 'EZACCUR', 'path': '/', 'secure': False, 'value': 'FC5593496F684496BFCCC3224A937579'},
        # #            {'domain': '172.16.1.100', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/ezaccur', 'secure': False, 'value': 'FC5593496F684496BFCCC3224A937579'}]
        # for cookie in cookies:
        #     self.driver.add_cookie(cookie)
        #
        # self.driver.get('http://172.16.1.100:8080/ezaccur/threatPrecaution')
        # self.driver.refresh()
        # sleep(3)

    def test_execute(self):
        self.driver.execute_script()

