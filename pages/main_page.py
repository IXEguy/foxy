""" The main page for Fox """

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.top_menu_bar import TopMenuBar


class MainPage(TopMenuBar):
    """Warning"""

    AGREE_CLOSE_BUTTON = (By.ID, "didomi-notice-agree-button")

    """ Subscribe Dialog"""
    CLOSE_SUBSCRIBE_NOW_BUTTON = (
        By.CSS_SELECTOR,
        "button.email-subscription-modal-close-button",
    )

    """ Search Fields """
    COUNTRY_FIELD = (By.ID, "resFormCountry_chosen")
    RENT_FROM_DROPDOWN = (By.ID, "resFormRentFrom_chosen")
    RENT_FROM_FIELD = (By.XPATH, '//*[@id="resFormRentFrom_chosen"]/div/div/input')
    RETURN_TO_DROPDOWN = (By.ID, "resFormReturnTo_chosen")
    RETURN_TO_FIELD = (By.XPATH, '//*[@id="resFormReturnTo_chosen"]/div/div/input')
    PICKUP_DATE_FIELD = (By.ID, "resFormPickUp")
    PICKUP_TIME_FIELD = (By.ID, "res_form_pick_up_time_chosen")
    DROPOFF_DATE_FIELD = (By.ID, "resFormDropOff")
    DROPOFF_TIME_FIELD = (By.ID, "res_form_drop_off_time_chosen")
    GET_RATES_BUTTON = (By.NAME, "singlebutton")

    # def __init__(self, driver):
    #     super().__init__(driver)

    @allure.step("Dismiss GDPR type warning, if shown")
    def dismiss_warning(self):
        """ Dismiss privacy/GDPR warning """
        self.click(self.AGREE_CLOSE_BUTTON)

    @allure.step("Dismiss email promo, if shown")
    def dismiss_email_subscription(self):
        """ Dismiss email subscription modal"""
        self.click(self.CLOSE_SUBSCRIBE_NOW_BUTTON)

    @allure.step(
        "Search with from: {from_airport} and to: {to_airport} between {start_date} and {end_date}"
    )
    def search(self, from_airport, to_airport, start_date, end_date):
        """
        Search for a rental based on criteria that was passed in
        :param from_airport: From airport, 3 letter code or city name
        :param to_airport:  To airport, 3 letter code or city name (Can be same as From)
        :param start_date: Start date for rental in mm/dd/yyyy format
        :param end_date: End date for rental in mm/dd/yyyy format
        :return: None
        """
        # TODO: Break this out into individual steps & add validation to fields
        self.click(self.RENT_FROM_DROPDOWN)
        self.clear_text(self.RENT_FROM_FIELD)
        self.fill_text(self.RENT_FROM_FIELD, from_airport + Keys.ENTER)

        self.click(self.RETURN_TO_DROPDOWN)
        self.clear_text(self.RETURN_TO_FIELD)
        self.fill_text(self.RETURN_TO_FIELD, to_airport + Keys.ENTER)

        self.clear_text(self.PICKUP_DATE_FIELD)
        self.fill_text(self.PICKUP_DATE_FIELD, start_date)

        self.clear_text(self.DROPOFF_DATE_FIELD)
        self.fill_text(self.DROPOFF_DATE_FIELD, end_date + Keys.TAB + Keys.TAB)

        self.click(self.GET_RATES_BUTTON)
        print("Done")
