import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.top_menu_bar import TopMenuBar


class MainPage(TopMenuBar):
    """ Warning"""
    AGREE_CLOSE_BUTTON = (By.ID, "didomi-notice-agree-button")

    """ Subscribe Dialog"""
    CLOSE_SUBSCRIBE_NOW_BUTTON = (By.CSS_SELECTOR, "button.email-subscription-modal-close-button")

    """ Login Fields """
    USERNAME_FIELD = (By.ID, "login-email")
    PASSWORD_FIELD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login-submit")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".login_error_message > div:nth-child(1)")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot-password-link")

    """ Search Fields """
    COUNTRY_FIELD = (By.ID, "resFormCountry_chosen")
    RENT_FROM_DROPDOWN = (By.ID, "resFormRentFrom_chosen")
    RENT_FROM_FIELD = (By.CSS_SELECTOR, "#resFormRentFrom_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
    RETURN_TO_DROPDOWN = (By.ID, "resFormReturnTo_chosen")
    RETURN_TO_FIELD = (By.CSS_SELECTOR, "#resFormReturnTo_chosen > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)")
    PICKUP_DATE_FIELD = (By.ID, "resFormPickUp")
    PICKUP_TIME_FIELD = (By.ID, "res_form_pick_up_time_chosen")
    DROPOFF_DATE_FIELD = (By.ID, "resFormDropOff")
    DROPOFF_TIME_FIELD = (By.ID, "res_form_drop_off_time_chosen")
    GET_RATES_BUTTON = (By.CSS_SELECTOR, "body > div.container-fluid > div:nth-child(2) > div > div > div >  div.carousel-container.carousel.margin_bottom > div.carousel-res-form.position-lg-absolute.position-md-absolute.position-sm-absolute > form > div:nth-child(9) > div.col-md-5.col-xs-12 > a")  #btn btn-primary res_form_get_rates

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Dismiss GDPR type warning, if shown")
    def dismiss_warning(self):
        # time.sleep(1)   # TODO: Switch to WebdriverWait
        # if self.is_elem_displayed(self._driver.find_element(*self.AGREE_CLOSE_BUTTON)):
        self.click(self.AGREE_CLOSE_BUTTON)

    @allure.step("Dismiss email promo, if shown")
    def dismiss_email_subscription(self):
        # time.sleep(1)   # TODO: Switch to WebdriverWait
        # if self.is_elem_displayed(self._driver.find_element(*self.CLOSE_SUBSCRIBE_NOW_BUTTON)):
        self.click(self.CLOSE_SUBSCRIBE_NOW_BUTTON)

    @allure.step("Log in with username: {username} and password: {password}")
    def login(self, username, password):
        self.click(self.LOGIN_DIALOG_OPEN_BUTTON)
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Search with from: {from_airport} and to: {to_airport} between {start_date} and {end_date}")
    def search(self, from_airport, to_airport, start_date, end_date):
        # TODO: Break this out into individual steps
        self.click(self.RENT_FROM_DROPDOWN)
        self.clear_text(self.RENT_FROM_FIELD)
        self.fill_text(self.RENT_FROM_FIELD, from_airport+Keys.ENTER)

        self.click(self.RETURN_TO_DROPDOWN)
        self.clear_text(self.RETURN_TO_FIELD)
        self.fill_text(self.RETURN_TO_FIELD, to_airport + Keys.ENTER)

        self.clear_text(self.PICKUP_DATE_FIELD)
        self.fill_text(self.PICKUP_DATE_FIELD, start_date)

        self.clear_text(self.DROPOFF_DATE_FIELD)
        self.fill_text(self.DROPOFF_DATE_FIELD, end_date+Keys.TAB+Keys.TAB)

        self.click(self.GET_RATES_BUTTON)
        print('Done')

    @allure.step("Get error message")
    def get_error_message(self):
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD_LINK)