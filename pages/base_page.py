"""
Base Page
This is the base page object for the page objects in this project
"""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import (
    StaleElementReferenceException,
)
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Wrapper for selenium operations"""

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def click(self, webelement):
        """Locates, highlights and clicks on the web element that was passed in"""
        element = self._wait.until(
            expected_conditions.element_to_be_clickable(webelement)
        )
        self._highlight_element(element, "green")
        element.click()

    def fill_text(self, webelement, txt):
        """Locates, highlights and fills in the text for the web element that was passed in"""
        text_field = self._wait.until(
            expected_conditions.element_to_be_clickable(webelement)
        )
        text_field.clear()
        self._highlight_element(text_field, "green")
        text_field.send_keys(txt)

    def clear_text(self, webelement):
        """Locates, highlights and clears out the text in the web element that was specified"""
        text_field = self._wait.until(
            expected_conditions.element_to_be_clickable(webelement)
        )
        text_field.clear()

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page"""
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def submit(self, webelement):
        """Highlights & submits the specified web element"""
        self._highlight_element(webelement, "green")
        webelement.submit()

    def get_text(self, webelement):
        """Highlights & returns the text in the specified web element"""
        text_object = self._wait.until(
            expected_conditions.visibility_of_element_located(webelement)
        )
        self._highlight_element(text_object, "green")
        return text_object.text

    def move_to_element(self, webelement):
        """Locates and moves to the specified web element"""
        action = ActionChains(self._driver)
        self._wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()

    def is_elem_displayed(self, webelement):
        """Returns a boolean indicating if the specified web element was displayed or not"""
        try:
            return webelement.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def _highlight_element(self, webelement, color):
        """Highlights the element undergoing an interaction for easier visual troubleshooting and verification"""
        original_style = webelement.get_attribute("style")
        new_style = (
            "background-color:yellow;border: 1px solid " + color + original_style
        )
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style
            + "');},0);",
            webelement,
        )
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style
            + "');},400);",
            webelement,
        )
