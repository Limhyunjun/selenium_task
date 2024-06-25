from conf.conftest import wait_for_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class BaseClass():

    def __init__(self):
        print('Create Driver')
        # ChromeService 객체 생성
        service = ChromeService(executable_path=ChromeDriverManager().install())

        # webdriver.Chrome에 service 객체 전달
        self.driver = webdriver.Chrome(service=service)

        # 창크기 최대화
        self.driver.maximize_window()

    def go_to_mainpage(self):
        self.driver.get("https://www.demoblaze.com/index.html")
        wait_for_element(self.driver, By.ID, 'signin2')


