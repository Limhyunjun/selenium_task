import time
from selenium.common.exceptions import TimeoutException

# 요소가 존재하는지 확인하는 함수
def wait_for_element(driver, by, value, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        elements = driver.find_elements(by, value)
        if len(elements) > 0:
            return elements[0]  # 요소가 발견되면 반환
        time.sleep(1)
    raise TimeoutException(f"Element with {by} = '{value}' not found within {timeout} seconds")




