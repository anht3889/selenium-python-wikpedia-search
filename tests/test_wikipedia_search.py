import pytest
import allure

from pages.main_page import MainPage
from utils.read_csv import ReadCSV

@pytest.mark.usefixtures("setup")
class TestSearch:

    @allure.title("Search matching a page title")
    @allure.description("This is test of searching a string which matches a page title")
    @pytest.mark.parametrize("data", ReadCSV.get_match_data())
    def test_search_match(self, data):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.type_search_box(data[0])
        main_page.click_search_page_item()
        
        assert main_page.get_page_title() == data[0] + ' - Search results - Wikipedia'
        assert main_page.is_search_exist_info_displayed()

    @allure.title("Search non-match")
    @allure.description("This is test of searching a string which doesn't match any page title")
    def test_search_non_match(self):
        search_term = 'This is from Anh Tran'
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.type_search_box(search_term)
        main_page.click_search_page_item()

        assert main_page.get_page_title() == search_term + ' - Search results - Wikipedia'
        assert main_page.is_search_not_match_info_displayed()

    @allure.title("Search with text more than 300 chars")
    @allure.description("This is test of searching a string which has more than 300 char length")
    def test_search_more_than_300_chars(self):
        search_term = 'But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids.'
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.type_search_box(search_term)
        main_page.click_search_page_item()

        assert main_page.is_max_length_message_displayed()