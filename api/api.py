import allure
import datetime
import logging
import requests

class Api:
    log_filename = datetime.datetime.now().strftime("%Y%m%d")
    logging.basicConfig(
        # log file will be created in "tests" directory. Feel free to change the path or filename
        filename=f"{log_filename}.log",
        format="%(asctime)s: %(levelname)s: %(message)s",
        level=logging.INFO
    )

    def __init__(self, config):
        self.endpoint = config['api_endpoint']
        self.logger = logging.getLogger("api")

    def get(self, params):
        return requests.get(self.endpoint, params=params)
    
    @allure.step("Send Get request for a simple search")
    def simple_search(self, search_term, action='query', list='search', format='json'):
        params = {'action': action, 'list': list, 'srsearch': search_term, 'format': format}
        resp = self.get(params)
        self.logger.info(resp.json())
        return resp
    
