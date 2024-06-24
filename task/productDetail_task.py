from conf.conftest import return_alert_text, accept_alert
from elements.productDetail_element import productDetailPageElement


class productDetailPageClass():
    '''
    init
    전달 받은 driver를 class 변수 driver에 옮김
    product_detail page에서 사용할 element class load
    '''
    def __init__(self, driver):
        self.driver = driver
        self.product_detail_element = productDetailPageElement(self.driver)

    '''
    add_to_cart
    addToCart 버튼 클릭 후 Product added 얼럿 노출 확인 후 닫기
    '''
    def add_to_cart(self):
        self.product_detail_element.get_add_to_cart_btn().click()
        assert return_alert_text(self.driver) == 'Product added.', 'if add to cart click, Product added. not exposed'
        accept_alert(self.driver)
