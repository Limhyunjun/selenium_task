from conf.conftest import get_timeStamp, return_alert_text, input_data, accept_alert, is_alert_present
from elements.landingPage_element import landingPage
from task.productDetail_task import productDetailPageClass
from selenium.common.exceptions import TimeoutException
import random
import time

class landingPageClass():

    def __init__(self, driver):
        self.driver = driver
        self.landing_page_element = landingPage(self.driver)

    def go_to_cartpage(self):
        # cart page 이동
        self.landing_page_element.get_cartPage().click()

    def sign_up(self):
        # sign up modal 진입 후 modal 노출 확인
        self.landing_page_element.get_sign_up().click()
        assert self.landing_page_element.get_modal_sign_up_btn(), 'signup modal에 signup 버튼을 찾을 수 없음(미달 미노출)'

        # id 겹치지않게 timestamp를 활용하여 생성
        # 비밀번호 조건이없으므로 id와 동일하게 설정
        self.id = f"test_{get_timeStamp()}"
        self.pw = self.id

        # userName , PW 입력
        input_data(self.landing_page_element.get_sign_up_modal_username(), self.id)
        input_data(self.landing_page_element.get_sign_up_modal_password(), self.pw)

        # signup 버튼 클릭 ( click() 먹히지 않아 javascript로 진행 )
        self.driver.execute_script("arguments[0].click();", self.landing_page_element.get_modal_sign_up_btn())

        # alert 문구 확인 후 alert 닫기
        alert_text = return_alert_text(self.driver)
        try:
            assert alert_text == 'Sign up successful.'
        except AssertionError:
            if alert_text == 'This user already exist.':
                raise Exception("already exist user")
            else:
                raise AssertionError('signup fail')
        finally:
            accept_alert(self.driver)
        # 빨라서 안 닫혔을 경우 5초간 다시 닫기 시도 후 실패 시 error raise
        count = 0
        while count < 5:
            if not is_alert_present(self.driver):
                break
            else:
                accept_alert(self.driver)
                time.sleep(1)
                count+=1

    # 로그인 상태 확인
    def check_logout_status(self):
        try:
            self.landing_page_element.get_log_out()
            return True
        except TimeoutException:
            return False

    def logout(self):
        self.landing_page_element.get_log_out().click()

    # 로그인 task
    def log_in(self):
        # login 된 상태면 logout 진행
        if self.check_logout_status():
            self.logout()

        # 로그인 버튼 찾고 존재하는지 확인
        assert self.landing_page_element.get_log_in(5), '5초간 login버튼 미노출'

        # 로그인 modal 진입
        self.landing_page_element.get_log_in().click()

        # 로그인 modal 대기
        self.landing_page_element.get_log_in_modal_label()

        # username, password 입력
        input_data(self.landing_page_element.get_log_in_modal_username(), self.id)
        input_data(self.landing_page_element.get_log_in_modal_password(), self.pw)

        # log in modal의 log in btn 클릭
        self.landing_page_element.get_modal_log_in_btn().click()

        try:
            assert self.landing_page_element.get_welcome().text == f"Welcome {self.id}"
        except AssertionError:
            if return_alert_text(self.driver) == 'Wrong password.':
                raise Exception("Wrong password.")
            elif return_alert_text(self.driver) == 'User does not exist.':
                raise Exception("User does not exist.")
            else:
                raise AssertionError('로그인 후 welcome id 노출 안됨(로그인이 안됬을수도 있음)')

    def add_product_to_cart(self,num):
        numbers = random.sample(range(1,len(self.landing_page_element.get_product_list())), num)
        productName = self.add_cart(numbers)
        return productName


    def add_cart(self,num):
        productDetailPage = productDetailPageClass(self.driver)
        productName = []
        for i in num:
            element_product = self.landing_page_element.get_product(i)
            productName.append(element_product.text)
            element_product.click()
            productDetailPage.add_to_cart()
            self.go_to_home()
            time.sleep(1)
        return productName

    def go_to_home(self):
        self.landing_page_element.get_product_logo().click()

