import time
from conf.conftest import wait_for_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        wait_for_element(self.driver, By.ID, 'signin2').click()
        signUpBtn = wait_for_element(self.driver, By.XPATH, "//button[contains(text(), 'Sign up')]")
        time.sleep(1)
        userName_space = wait_for_element(self.driver, By.ID, 'sign-username')
        print(userName_space)
        userName_space.clear()
        userName_space.send_keys('qtqtqt12341415231')
        password_space = wait_for_element(self.driver, By.ID, 'sign-password')
        password_space.clear()
        password_space.send_keys('qtqtqt12341425631')
        time.sleep(1)
        print(signUpBtn)
        self.driver.execute_script("arguments[0].click();", signUpBtn)
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        try:
            assert self.driver.switch_to.alert.text == 'Sign up successful.'
        except AssertionError:
            if self.driver.switch_to.alert.text == 'This user already exist.':
                raise Exception("already exist user")


