""" Objects and methods for the Results page """
import allure
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions

from pages.top_menu_bar import TopMenuBar


class ResultsPage(TopMenuBar):
    """Results page - Where results for the search are displayed"""

    RESULTS_TITLE = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[2]")

    @allure.step("Get projects' page title")
    def get_title(self):
        """ Returns the title of the page as displayed, after the Home keyword """
        return self.get_text(self.RESULTS_TITLE)
