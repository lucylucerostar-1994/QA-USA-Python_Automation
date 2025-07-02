import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage

# URBAN_ROUTES_URL imports from data
# Check if the server is running due to Urban Routes server expiring often

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        url = data.URBAN_ROUTES_URL
        if helpers.is_url_reachable(url):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Each function has a 'self' parameter

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        assert routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        phone_number = data.PHONE_NUMBER
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_current_payment_method() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        message = data.MESSAGE_FOR_DRIVER
        routes_page.set_message_for_driver(message)
        assert routes_page.get_message_for_driver() == message

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        routes_page.click_blanket_and_handkerchiefs_option()
        assert routes_page.get_blanket_and_handkerchiefs_option_checked()

    # uses a range loop and a pass statement
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.select_supportive_plan()
        number_of_ice_creams = 2
        routes_page.add_ice_cream(number_of_ice_creams)
        assert routes_page.get_amount_of_ice_cream() == 2

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        message = data.MESSAGE_FOR_DRIVER
        routes_page.set_message_for_driver(message)
        routes_page.click_order_taxi_button()
        assert routes_page.is_order_taxi_popup()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
