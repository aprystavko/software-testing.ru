import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver(request):
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.addfinalizer(driver.quit)
    return driver


def test_example(driver):
    driver.get('https://www.google.com/')
    search_input = driver.find_element(By.NAME, 'q')
    search_input.send_keys('Python')
    search_input.submit()

    WebDriverWait(driver, 10).until(EC.title_is)('Python - Google Search')
    time.sleep(5)
    driver.close()
