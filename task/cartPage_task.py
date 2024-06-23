from conf.conftest import wait_for_element
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class cartPageClass():

    def __init__(self,driver):
        self.driver = driver

    def go_to_cartpage(self):
        # ChromeService 객체 생성
        wait_for_element(self.driver, By.ID, 'cartur').click()

    def confirm_cart(self, name):
        for i in name:
            assert wait_for_element(self.driver, By.XPATH, f"//td[text()='{i}']")

    def clear_cart(self):
        try:
            element = wait_for_element(self.driver, By.XPATH,"//a[contains(@onclick, 'deleteItem') and contains(text(), 'Delete')]", 5)
            element.click()
            time.sleep(2)
            self.clear_cart()
        except TimeoutException:
            print('no cart list')

    def delete_cart_list(self):
        wait_for_element(self.driver, By.XPATH, "//a[contains(@onclick, 'deleteItem') and contains(text(), 'Delete')]",5).click()



