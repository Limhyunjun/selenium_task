import time
from conf.conftest import wait_for_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class landingPageTask():

    def __init__(self):
        print('init')

    def go_to_mainpage(self):
        # ChromeService 객체 생성
        service = ChromeService(executable_path=ChromeDriverManager().install())

        # webdriver.Chrome에 service 객체 전달
        self.driver = webdriver.Chrome(service=service)

        self.driver.get("https://www.demoblaze.com/index.html")
        a = wait_for_element(self.driver, 'id', 'signin2')
        print(a)
    def sign_up(self):
        wait_for_element(self.driver, 'id', 'signin2').click()
        return wait_for_element(self.driver, By.CLASS_NAME, 'btn-primary')


