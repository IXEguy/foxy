""" Objects and methods for the Results page """
import allure
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions

from pages.top_menu_bar import TopMenuBar


class ResultsPage(TopMenuBar):
    """Results page - Where results for the search are displayed"""

    RESULTS_TITLE = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[2]")
    RESULTS_ALL = (By.ID, "addVehicle")
    LOADING_GIF = (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/img")
    LOADING_DIV = (By.ID, "mtitle")

    @allure.step("Get projects' page title")
    def get_title(self) -> str:
        """ Returns the title of the page as displayed, after the Home keyword """
        return self.get_text(self.RESULTS_TITLE)

    @allure.step("Wait for search to complete")
    def wait_for_search_completion(self) -> bool:
        """ Wait for the search to complete """
        return self.wait_until_elem_is_not_displayed(self.LOADING_GIF)

    @allure.step("Results shown")
    def results_shown(self) -> bool:
        """
        Returns if search results are displayed
        :return: bool of display status
        """
        return self.is_elem_displayed(self._driver.find_element(*self.RESULTS_ALL))
