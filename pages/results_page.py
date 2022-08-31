import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


from pages.top_menu_bar import TopMenuBar


class ResultsPage(TopMenuBar):
    """ Results page - Where results for the search are displayed """

    # RESULTS_TITLE = (By.CSS_SELECTOR, ".content > div:nth-child(1) > div:nth-child(2) > h1:nth-child(1)")
    RESULTS_TITLE = (By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[2]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get projects' page title")
    def get_title(self):
        return self.get_text(self.RESULTS_TITLE)
