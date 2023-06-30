import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageBase:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def open(self):
        self.driver.open()

    @allure.step("Wait for element displayed")
    def wait_element_displayed(self, *selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(selector))
    
    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title
