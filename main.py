import logging
from selenium import webdriver
from pages import UrbanRoutesPage
from data import (
logging.basicConfig(level=logging.INFO)

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if not helpers.is_url_reachable(URBAN_ROUTES_URL):
            raise Exception("Server is not reachable. Aborting tests.")
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        # Add in S8
        pass

    def test_select_plan(self):
         # Add in S8
        pass

    def test_fill_phone_number(self):
         # Add in S8
        pass

    def test_fill_card(self):
         # Add in S8
        pass

    def test_comment_for_driver(self):
         # Add in S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
         # Add in S8
        pass

    def test_order_2_ice_creams(self):
        for i in range(2):
            pass

    def test_car_search_model_appears(self):
        pass

    @classmethod
    def teardown_class(cls):
        logging.info("Closing the browser.")
        cls.driver.quit()

