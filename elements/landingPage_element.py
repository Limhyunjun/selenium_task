from conf.conftest import wait_for_element, scroll_to_element, wait_for_elements
from selenium.webdriver.common.by import By


class landingPage():
    # 상단 product store 로고
    product_store_logo = "//a[@class='nav-link' and @href='index.html']"
    # 상단 네비게이션 signup
    sign_up_btn = 'signin2'
    # 상단 네비게이션 login
    log_in_btn = 'login2'
    # 상단 네비게이션 logout
    log_out_btn = 'logout2'
    # 상단 네비게이션 Cart
    cart_btn = 'cartur'
    # 상단 네비게이션 welcome
    welcome = 'nameofuser'
    # signup modal의 signup 버튼
    modal_sign_up_btn = "//button[contains(text(), 'Sign up')]"
    # signup modal의 username 입력 영역
    sign_up_modal_username = 'sign-username'
    # signup modal의 password 입력 영역
    sign_up_modal_password = 'sign-password'
    # login modal의 label 영역
    log_in_modal_label = "logInModalLabel"
    # login modal의 username 입력 영역
    log_in_modal_username = 'loginusername'
    # login modal의 password 입력 영역
    log_in_modal_password = 'loginpassword'
    # login modal의 login 버튼
    modal_log_in_btn = "//button[contains(text(), 'Log in')]"
    # product list
    product_list = 'h-100'

    def __init__(self,driver):
        self.driver = driver

    # 상단 product store 로고
    def get_product_logo(self):
        return wait_for_element(self.driver, By.XPATH, self.product_store_logo)

    # 상단 네비게이션 sign up element 반환
    def get_sign_up(self):
        return wait_for_element(self.driver,By.ID,self.sign_up_btn)

    # 상단 네비게이션 login element 반환
    def get_log_in(self, time=3):
        return wait_for_element(self.driver, By.ID, self.log_in_btn, time)

    # 상단 네비게이션 logout element 반환
    def get_log_out(self, time=3):
        return wait_for_element(self.driver, By.ID, self.log_out_btn, time)

    # 상단 네비게이션 Cart element 반환
    def get_cartPage(self):
        return wait_for_element(self.driver, By.ID, self.cart_btn)

    # 상단 welcome 문구 element 반환
    def get_welcome(self):
        return wait_for_element(self.driver,By.ID,self.welcome)

    # signup modal의 signup btn element 반환
    def get_modal_sign_up_btn(self):
        return wait_for_element(self.driver, By.XPATH, self.modal_sign_up_btn)

    # signup modal의 username 입력 영역 element 반환
    def get_sign_up_modal_username(self):
        return wait_for_element(self.driver, By.ID, self.sign_up_modal_username)

    # signup modal의 password 입력 영역 element 반환
    def get_sign_up_modal_password(self):
        return wait_for_element(self.driver, By.ID, self.sign_up_modal_password)

    # login modal의 label element 반환
    def get_log_in_modal_label(self):
        return wait_for_element(self.driver, By.ID, self.log_in_modal_label)

    # login modal의 username 입력 영역 element 반환
    def get_log_in_modal_username(self):
        return wait_for_element(self.driver, By.ID, self.log_in_modal_username)

    # login modal의 password 입력 영역 element 반환
    def get_log_in_modal_password(self):
        return wait_for_element(self.driver, By.ID, self.log_in_modal_password)

    # login modal의 login btn element 반환
    def get_modal_log_in_btn(self):
        return wait_for_element(self.driver, By.XPATH, self.modal_log_in_btn)

    # product list element 반환
    def get_product_list(self):
        return wait_for_elements(self.driver, By.CLASS_NAME, self.product_list)

    # 전달받은 n번째 product 보일때까지 scroll 하고 element 반환
    def get_product(self, num):
        return scroll_to_element(self.driver, By.XPATH, f"//a[@href='prod.html?idp_={num}' and @class='hrefch']")