import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function")
def driver():
    #Cоздать и закрыть по завершении экземпляр Chrome
    chrome_options = ChromeOptions()

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()