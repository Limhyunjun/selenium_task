from conf.conftest import wait_for_element, is_alert_present, wait_for_elements, scroll_to_element
from task.productDetail import productDetailPageClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import random
import time

class landingPageClass():

    def __init__(self, driver):
        self.driver = driver

    def sign_up(self):
        wait_for_element(self.driver, By.ID, 'signin2').click()
        signUpBtn = wait_for_element(self.driver, By.XPATH, "//button[contains(text(), 'Sign up')]")
        #id 겹치지않게 timestamp를 활용하여 생성
        now = datetime.now()
        self.id = f"test_{now.strftime('%Y%m%d%H%M%S')}"
        # 비밀번호 조건이없으므로 id와 동일하게 설정
        self.pw = self.id
        userName_space = wait_for_element(self.driver, By.ID, 'sign-username')
        userName_space.clear()
        userName_space.send_keys(self.id)
        password_space = wait_for_element(self.driver, By.ID, 'sign-password')
        password_space.clear()
        password_space.send_keys(self.pw)
        self.driver.execute_script("arguments[0].click();", signUpBtn)
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        try:
            assert alert.text == 'Sign up successful.'
        except AssertionError:
            if self.alert.text == 'This user already exist.':
                raise Exception("already exist user")
        alert.accept()
        while True:
            if not is_alert_present(self.driver):
                break
        print('done sign up')

    def check_login_status(self):
        try:
            wait_for_element(self.driver, By.ID, 'logout2',2)
            return True
        except TimeoutException:
            return False

    def logout(self):
        wait_for_element(self.driver, By.ID, 'logout2').click()

    # 로그인 task
    def log_in(self):
        if self.check_login_status():
            self.logout()
        # 로그인 버튼 찾고 존재하는지 확인
        logInBtn = wait_for_element(self.driver, By.ID, 'login2')
        assert logInBtn
        # 로그인 modal 진입
        logInBtn.click()
        # 로그인 modal 진입 대기
        wait_for_element(self.driver, By.ID, "logInModalLabel")
        # 회원가입한 정보로 username, password 입력
        userName_space = wait_for_element(self.driver, By.ID, 'loginusername')
        userName_space.clear()
        userName_space.send_keys(self.id)
        password_space = wait_for_element(self.driver, By.ID, 'loginpassword')
        password_space.clear()
        password_space.send_keys(self.pw)
        logInBtn2 = wait_for_element(self.driver, By.XPATH, "//button[contains(text(), 'Log in')]")
        logInBtn2.click()
        try:
            welcomeWorld = wait_for_element(self.driver, By.ID, 'nameofuser')
            assert welcomeWorld.text == f"Welcome {self.id}"
        except:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            try:
                assert alert.text == 'Sign up successful.'
            except AssertionError:
                if self.alert.text == 'Wrong password.':
                    raise Exception("Wrong password.")
                elif self.alert.text == 'User does not exist.':
                    raise Exception("User does not exist.")
            alert.accept()

    def add_product_to_cart(self,num):
        a = wait_for_elements(self.driver, By.CLASS_NAME, 'h-100')
        numbers = random.sample(range(1,len(a)), num)
        productName = self.add_cart(numbers)
        return productName


    def add_cart(self,num):
        productDetailPage = productDetailPageClass(self.driver)
        productName = []
        for i in num:
            element_product = scroll_to_element(self.driver,By.XPATH, f"//a[@href='prod.html?idp_={i}' and @class='hrefch']")
            productName.append(element_product.text)
            element_product.click()
            productDetailPage.add_to_cart()
            self.go_to_home()
            time.sleep(1)
        return productName

    def go_to_home(self):
        wait_for_element(self.driver, By.XPATH, "//a[@class='nav-link' and @href='index.html']").click()

