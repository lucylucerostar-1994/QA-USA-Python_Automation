import logging
from selenium import webdriver

import data
import helpers

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        if not helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            raise Exception("Server is not reachable. Aborting tests.")
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        # Add in S8
        print("Test set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Test select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Test phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Test fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Test for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Test order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        print("Test order 2 ice creams")
        for i in range(2):
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Test search model")
        pass

    @classmethod
    def teardown_class(cls):
        logging.info("Closing the browser.")
        cls.driver.quit()

