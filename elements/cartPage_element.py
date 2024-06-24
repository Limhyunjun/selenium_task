from conf.conftest import wait_for_element, wait_for_elements
from selenium.webdriver.common.by import By


class cartPageElement():

    # delete 버튼
    delete_btn = "//a[contains(@onclick, 'deleteItem') and contains(text(), 'Delete')]"

    def __init__(self,driver):
        self.driver = driver

    # 전달 받은 배열의 title element 반환
    def get_exist_title(self, name):
        return wait_for_element(self.driver, By.XPATH, f"//td[text()='{name}']")

    # delete btn element 반환
    def get_delete_btn(self):
        return wait_for_element(self.driver, By.XPATH, self.delete_btn,5)

    # n번째 delete 버튼 element 반환
    def get_delete_btns(self,num):
        return wait_for_elements(self.driver, By.XPATH, self.delete_btn,5)[num]
