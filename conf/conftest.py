import time
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

@pytest.fixture(scope='session')
def set_get_id_pw():
    id_pw = {"id": "asd", "pw": "asd"}
    return id_pw

def wait_for_element(driver, by, value, timeout=5):
    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, value))
    )
    return element

# WebDriverWait는 단일만 반환해서 다중 요소가 있을때 사용
def wait_for_elements(driver, by, value, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        elements = driver.find_elements(by, value)
        if len(elements) > 0:
            return elements  # 요소가 발견되면 반환
        time.sleep(1)
    raise TimeoutException(f"Element with {by} = '{value}' not found within {timeout} seconds")

def is_alert_present(driver):
    try:
        driver.switch_to.alert
        return True
    except NoAlertPresentException:
        return False

def return_alert_text(driver):
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    return driver.switch_to.alert.text

def accept_alert(driver):
    WebDriverWait(driver, 10).until(EC.alert_is_present()).accept()

def scroll_to_element(driver, by, value, timeout=10):
    element = None
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
    except Exception as e:
        print(f"An error occurred: {e}")
    return element

# timestamp 반환
def get_timeStamp():
    now = datetime.now()
    return now.strftime('%Y%m%d%H%M%S')

# 전달받은 data를 전달받은 element 초기화 후 입력
def input_data(element,data):
    element.clear()
    element.send_keys(data)



