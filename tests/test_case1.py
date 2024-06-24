import pytest
from task.landingPage_task import landingPageClass
from task.cartPage_task import cartPageClass
from conf.conftest import set_get_id_pw
from utilities.baseclass import BaseClass

""" 
TC001 - 회원가입 테스트
사이트에서 사용자 회원가입이 정상적인지 확인
"""
# @pytest.mark.skip
def test_TC001(set_get_id_pw):
    # 사이트에서 사용자 가입이 가능하다.
    baseclass = BaseClass()
    #main page 이동
    baseclass.go_to_mainpage()
    landingPage = landingPageClass(baseclass.driver)
    landingPage.sign_up()
    # 회원 가입 후 진행하는 다른 TC에 id pw 사용을 위한 설정
    set_get_id_pw['id'] = landingPage.id
    set_get_id_pw['pw'] = landingPage.pw

""" 
TC002 - 로그인 테스트
사이트에서 사용자 로그인이 가능한지 확인
TC 1번에 이어 연속으로 수행되어지면 생성한 계정을 이용
로그인 테스트만 수행되어지면 default 계정인 asd/asd 계정으로 로그인
"""
# @pytest.mark.skip
def test_TC002(set_get_id_pw):
    # 사이트에서 사용자 가입이 가능하다.
    baseclass = BaseClass()
    # main page 이동
    baseclass.go_to_mainpage()
    landingPage = landingPageClass(baseclass.driver)
    landingPage.id = set_get_id_pw['id']
    landingPage.pw = set_get_id_pw['pw']
    landingPage.log_in()

""" 
TC003 - 제품 장바구니 추가
사이트에서 제품을 장바구니에 3개이상 추가 할 수 있는지 확인
해당 테스트만 수행되어지면 default 계정인 asd/asd 계정으로 로그인
"""
# @pytest.mark.skip
def test_TC003(set_get_id_pw):
    baseclass = BaseClass()
    # main page 이동
    baseclass.go_to_mainpage()
    landingPage = landingPageClass(baseclass.driver)
    landingPage.id = set_get_id_pw['id']
    landingPage.pw = set_get_id_pw['pw']
    landingPage.log_in()
    landingPage.go_to_cartpage()
    cartPage = cartPageClass(baseclass.driver)
    cartPage.clear_cart()
    landingPage.go_to_home()
    landingPage.add_product_to_cart(3)


""" 
TC004 - 과제 요구사항 flow
1. https://www.demoblaze.com/index.html 사이트에서 사용자 가입(SignUp) 진행
2. 가입 완료 후 가입한 ID,PWD로 로그인(Log in)을 수행
3. 로그인 완료 후 제품을 클릭하여 제품 설명 페이지로 이동
4. 제품 페이지에서 "Add to cart" 클릭하여 제품을 Cart에 저장
5. 다른 제품을 3가지 이상 Cart에 저장
6. 상단 Cart 메뉴를 클릭하여 Cart 페이지에 정상적으로 제품 저장 확인
7. Cart 제품 중 1가지 이상 삭제 ( 전체 삭제 )
"""
# @pytest.mark.skip
def test_TC004(set_get_id_pw):
    # 1. https://www.demoblaze.com/index.html 사이트에서 사용자 가입(SignUp) 진행
    baseclass = BaseClass()
    baseclass.go_to_mainpage()
    landingPage = landingPageClass(baseclass.driver)
    landingPage.sign_up()
    # 2. 가입 완료 후 가입한 ID,PWD로 로그인(Log in)을 수행
    landingPage.log_in()
    landingPage.go_to_home()
    # 3. 로그인 완료 후 제품을 클릭하여 제품 설명 페이지로 이동
    # 4. 제품 페이지에서 "Add to cart" 클릭하여 제품을 Cart에 저장
    # 5. 다른 제품을 3가지 이상 Cart에 저장
    productName = landingPage.add_product_to_cart(3)
    # 6. 상단 Cart 메뉴를 클릭하여 Cart 페이지에 정상적으로 제품 저장 확인
    landingPage.go_to_cartpage()
    cartPage = cartPageClass(baseclass.driver)
    cartPage.confirm_cart(productName)
    # 7. Cart 제품 중 1가지 이상 삭제 ( 전체 삭제 )
    cartPage.clear_cart()
    landingPage.go_to_home()
