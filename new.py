# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# import pytest
#
# @pytest.fixture()
# def browser():
#     options = Options()
#     options.add_argument('--headless')
#     chrome_browser = webdriver.Chrome(options=options)
#     # service = Service(executable_path=ChromeDriverManager().install())
#     return chrome_browser
#
# def test_button_exist(browser):
#     browser.get("https://www.qa-practice.com/elements/button/simple")
#     assert browser.find_element(By.ID,'submit-id-submit').is_displayed()


import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1280,800")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options= chrome_options)

driver.get("https://www.qa-practice.com/elements/button/simple")