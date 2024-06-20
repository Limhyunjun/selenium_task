from conf.conftest import wait_for_element


class landingPage():

    def __init__(self):
        print('init')
    # landing page element 변수

    # signup element
    signup = 'signin2'

    # signup element get
    def get_sign_up_element(self):
        return wait_for_element(self,'id',self.signup)


