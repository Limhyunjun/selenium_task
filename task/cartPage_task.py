from elements.cartPage_element import cartPageElement
from selenium.common.exceptions import TimeoutException
import time

class cartPageClass():
    '''
    init
    전달 받은 driver를 class 변수 driver에 옮김
    product_detail page에서 사용할 element class load
    '''
    def __init__(self,driver):
        self.driver = driver
        self.cart_page_element = cartPageElement(self.driver)

    def confirm_cart(self, name):
        # 전달 받은 title이 page에 존재하는지 확인
        for i in name:
            assert self.cart_page_element.get_exist_title(i), f'{i}이 존재하지 않습니다.'

    def clear_cart(self):
        # cart page에 존재하는 모든 list delete
        try:
            element = self.cart_page_element.get_delete_btn()
            element.click()
            time.sleep(2)
            self.clear_cart()
        except TimeoutException:
            print('list clear confirm')

    def delete_cart_list(self,num):
        # n번 list delete
        self.cart_page_element.get_delete_btns(num).click()



