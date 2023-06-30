import allure
from base.base_page import PageBase
from locators.locators import SearchLocators

class MainPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter search term")
    def type_search_box(self, text):
        self.driver.find_element(*SearchLocators.search_textbox).send_keys(text)

    @allure.step("Click Search button")
    def click_search_button(self):
        self.driver.find_element(*SearchLocators.search_button).click()

    @allure.step("Click Search for pages row in Search dropdown list")
    def click_search_page_item(self):
        self.driver.find_element(*SearchLocators.search_page_li).click()

    def is_search_results_info_displayed(self):
        return self.driver.find_element(*SearchLocators.search_results_info).is_displayed()
    
    def is_max_length_message_displayed(self):
        return self.driver.find_element(*SearchLocators.max_length_warning_message).is_displayed()
    
    def is_search_exist_info_displayed(self):
        return self.driver.find_element(*SearchLocators.search_exist_info).is_displayed()
    
    def is_search_not_match_info_displayed(self):
        return self.driver.find_element(*SearchLocators.search_not_match_info).is_displayed()
