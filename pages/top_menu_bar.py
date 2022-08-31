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

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Login button")
    def click_login(self):
        self.click(self.LOGIN_DIALOG_OPEN_BUTTON)

    @allure.step("Click Register button")
    def click_home(self):
        self.click(self.HOME_LINK)
