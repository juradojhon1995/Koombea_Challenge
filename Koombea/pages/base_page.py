from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """Encuentra un elemento con espera explícita"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        """Hace clic en un elemento"""
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        """Envía texto a un campo"""
        self.find_element(locator).send_keys(text)

