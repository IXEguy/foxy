""" Elements from the top bars that are persist across pages. """

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TopMenuBar(BasePage):
    """Top menu bar - The bar that appears on the top of the page prior to login """
    LOGIN_DIALOG_OPEN_BUTTON = (By.CSS_SELECTOR, ".login-link")
    HOME_LINK = (By.LINK_TEXT, "HOME")
    DEALS_LINK = (By.LINK_TEXT, "DEALS")
    LOCATIONS_LINK = (By.LINK_TEXT, "LOCATIONS")
    FOX_REWARDS_LINK = (By.LINK_TEXT, "FOX REWARDS")

    """ Login Fields """
    USERNAME_FIELD = (By.ID, "login-email")
    PASSWORD_FIELD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login-submit")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".login_error_message > div:nth-child(1)")
    FORGOT_PASSWORD_LINK = (By.ID, "forgot-password-link")

    @allure.step("Click Login button")
    def click_login(self):
        """ Click on the login button to open the login modal """
        self.click(self.LOGIN_DIALOG_OPEN_BUTTON)

    @allure.step("Log in with username: {username} and password: {password}")
    def login(self, username, password):
        """
        Login using the provided username and password
        :param username: Username for the user
        :param password: Password for the user
        :return:None
        """
        self.click(self.LOGIN_DIALOG_OPEN_BUTTON)
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Get error message")
    def get_error_message(self):
        """
        Return the text in the Login error message

        :return: None
        """
        return self.get_text(self.LOGIN_ERROR_MESSAGE)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self):
        """
        Click on the forgot password link
        :return: None
        """
        self.click(self.FORGOT_PASSWORD_LINK)

    @allure.step("Go back Home")
    def click_home(self):
        """ Navigate back to the Home page view """
        self.click(self.HOME_LINK)
