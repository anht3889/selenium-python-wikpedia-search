from selenium.webdriver.common.by import By

class SearchLocators:
    search_textbox = (By.NAME,'search')   
    search_button = (By.CSS_SELECTOR,'.cdx-search-input__end-button')
    search_page_li = (By.XPATH, "//li[contains(@class,'cdx-menu-item')]//span[contains(text(), 'Search for pages containing')]")
    search_results_info = (By.CLASS_NAME, 'mw-search-results-info')
    search_exist_info = (By.CLASS_NAME, 'mw-search-exists')
    search_not_match_info = (By.XPATH, "//i[starts-with(., 'The page') and contains(., 'does not exist')]")
    max_length_warning_message = (By.XPATH, "//p[contains(., 'An error has occurred while searching: Search request is longer than the maximum allowed length.')]")