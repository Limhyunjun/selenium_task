import pytest
import time
from task.landingPage_task import landingPageTask


def test_login_TC001():
    # 사이트에서 사용자 가입이 가능하다.
    task = landingPageTask()
    #main page 이동
    task.go_to_mainpage()
    task.sign_up()
    time.sleep(10)


if __name__ == "__main__":
    test_login_TC001()