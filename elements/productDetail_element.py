from conf.conftest import wait_for_element
from selenium.webdriver.common.by import By

class productDetailPageElement():

    # addToCart 버튼
    addToCart = "//a[contains(@onclick, 'addToCart')]"

    def __init__(self, driver):
        self.driver = driver

    # add to cart btn element 반환
    def get_add_to_cart_btn(self):
        return wait_for_element(self.driver, By.XPATH, self.addToCart)
