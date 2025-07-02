import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Addresses
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD =  (By.ID, 'to')
    # Tariff and call button
    SUPPORTIVE_PLAN_CARD = (By.XPATH, '//div[contains(text(), "Supportive")]')
    SUPPORTIVE_PLAN_CARD_PARENT = (By.XPATH, '//div[contains(text(), "Supportive")]//..')
    ACTIVE_PLAN_CARD = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    # Phone number
    PHONE_NUMBER_CONTROL = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Phone number")]')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    PHONE_CODE_INPUT = (By.ID, 'code')
    PHONE_NUMBER_NEXT_BUTTON = (By.CSS_SELECTOR, '.full')
    PHONE_NUMBER_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    PHONE_NUMBER = (By.CLASS_NAME, 'np-text')
    # Credit card
    PAYMENT_METHOD_SELECT = (By.XPATH, '//div[@class="pp-button filled"]//div[contains(text(), "Payment method")]')
    ADD_CARD_CONTROL = (By.XPATH, '//div[contains(text(), "Add card")]')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CODE_INPUT = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    CARD_CREDENTIALS_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Link")]')
    CLOSE_BUTTON_PAYMENT_METHOD = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    CURRENT_PAYMENT_METHOD = (By.CLASS_NAME, 'pp-value-text')
    # Options and orders

    MESSAGE_FOR_DRIVER = (By.ID, 'comment')
    OPTION_SWITCHES = (By.CLASS_NAME, 'switch')
    OPTION_SWITCHES_INPUTS = (By.CLASS_NAME, 'switch-input')
    ADD_ITEM_OPTION = (By.CLASS_NAME, 'counter-plus')
    AMOUNT_OF_ITEM_OPTION = (By.CLASS_NAME, 'counter-value')

    ORDER_CAR_BUTTON = (By.CLASS_NAME, 'smart-button-wrapper')
    ORDER_POPUP = (By.CLASS_NAME, 'order-body')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.FROM_FIELD))
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        to_field = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.TO_FIELD))
        to_field.send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.CALL_TAXI_BUTTON))
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def set_route(self, from_address: object, to_address: object) -> None:
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    # Check if the Supportive tariff is selected
    def select_supportive_plan(self):
        if self.driver.find_element(*self.SUPPORTIVE_PLAN_CARD_PARENT).get_attribute("class") != "tcard active":
            card = WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.SUPPORTIVE_PLAN_CARD))
            self.driver.execute_script("arguments[0].scrollIntoView();", card)
            card.click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_CARD).text

    def set_phone(self, number):
        self.driver.find_element(*self.PHONE_NUMBER_CONTROL).click()
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(number)
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_CODE_INPUT).send_keys(code)
        self.driver.find_element(*self.PHONE_NUMBER_CONFIRM_BUTTON).click()

    def get_phone(self):
        return self.driver.find_element(*self.PHONE_NUMBER).text

    def set_card(self, card_number, code):
        self.driver.find_element(*self.PAYMENT_METHOD_SELECT).click()
        time.sleep(3)
        self.driver.find_element(*self.ADD_CARD_CONTROL).click()
        self.driver.find_element(*self.CARD_NUMBER_INPUT).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE_INPUT).send_keys(code)
        # TAB
        self.driver.find_element(*self.CARD_CREDENTIALS_CONFIRM_BUTTON).click()
        self.driver.find_element(*self.CLOSE_BUTTON_PAYMENT_METHOD).click()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.CURRENT_PAYMENT_METHOD).text

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER).get_property('value')

    def click_blanket_and_handkerchiefs_option(self):
        switches = self.driver.find_elements(*self.OPTION_SWITCHES)
        switches[0].click()
        self.get_blanket_and_handkerchiefs_option_checked()

    def get_blanket_and_handkerchiefs_option_checked(self):
        switches = self.driver.find_elements(*self.OPTION_SWITCHES_INPUTS)
        return switches[0].get_property('checked')

    def add_ice_cream(self, amount: int):
        option_add_controls = self.driver.find_elements(*self.ADD_ITEM_OPTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", option_add_controls[0])
        for count in range(amount):
            option_add_controls[0].click()

    def get_amount_of_ice_cream(self):
        return int(self.driver.find_elements(*self.AMOUNT_OF_ITEM_OPTION)[0].text)

    def click_order_taxi_button(self):
        self.driver.find_element(*self.ORDER_CAR_BUTTON).click()

    def is_order_taxi_popup(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.ORDER_POPUP))
        return self.driver.find_element(*self.ORDER_POPUP).is_displayed()