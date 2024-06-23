from conf.conftest import wait_for_element, return_alert_text, accept_alert
from selenium.webdriver.common.by import By

class productDetailPageClass():

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        wait_for_element(self.driver, By.XPATH, "//a[contains(@onclick, 'addToCart')]").click()
        assert return_alert_text(self.driver) == 'Product added.'
        accept_alert(self.driver)