import pytest
import allure

from api.api import Api
from utils.read_csv import ReadCSV

class TestAPI:
    @allure.title("API - Valid simple search")
    @allure.description("This is test of sending GET api to do a valid simple search")
    def test_simple_search(self, config):
        search_term = "Company"
        api = Api(config)
        resp = api.simple_search(search_term)
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
        assert not(resp.json()['query']['search'] is None), "Search results not found"

    @allure.title("API - Empty search")
    @allure.description("This is test of sending GET api to do a empty search")
    def test_empty_search(self, config):
        search_term = ""
        api = Api(config)
        resp = api.simple_search(search_term)
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
        assert (resp.json()['error']['code'] == "missingparam"), "Missing param error not found"

    @allure.title("API - Invalid param action")
    @allure.description("This is test of sending GET api with invalid param action")
    def test_invalid_action(self, config):
        search_term = "abc"
        api = Api(config)
        resp = api.simple_search(search_term, "invalid")
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
        assert (resp.json()['error']['code'] == "badvalue"), "badvalue not found"
        assert ('Unrecognized value for parameter "action"' in resp.json()['error']['info']), "error info incorrect"

    @allure.title("API - Invalid param list")
    @allure.description("This is test of sending GET api with invalid param list")
    def test_invalid_list(self, config):
        search_term = "abc"
        api = Api(config)
        resp = api.simple_search(search_term, list = "invalid")
        assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
        assert (resp.json()['warnings']['main']['*'] == "Unrecognized parameter: srsearch."), "warnings not found"
        assert ('Unrecognized value for parameter "list"' in resp.json()['warnings']['query']["*"]), "warnings info incorrect"