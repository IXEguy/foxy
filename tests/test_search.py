""" Tests for exercising and validating the Find Rates functionality """
from datetime import datetime, timedelta

import allure
import pytest
from assertpy import assert_that

from tests.test_base import BaseTest


dt_now = datetime.now()

search_criteria = [
    (
        "SAN",
        "LAX",
        (dt_now + timedelta(days=1)).strftime("%m/%d/%Y"),
        (dt_now + timedelta(days=7)).strftime("%m/%d/%Y"),
    ),
    (
        "LAX",
        "PHX",
        (dt_now + timedelta(days=1)).strftime("%m/%d/%Y"),
        (dt_now + timedelta(days=30)).strftime("%m/%d/%Y"),
    ),
]


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Functional")
@allure.feature("Search")
@pytest.mark.functional
class TestSearch(BaseTest):
    """Validate various search option combinations"""

    @allure.title("Search for a rental being returned to origin")
    @pytest.mark.parametrize(
        "from_airport, start_date, end_date",
        [element[1:] for element in search_criteria],  # strip first airport out
    )
    @pytest.mark.run(order=1)
    def test_search_return_origin(self, from_airport, start_date, end_date):
        """Search with from and to airport being different"""
        self.pages["home_page"].dismiss_warning()
        self.pages["home_page"].dismiss_email_subscription()
        self.pages["home_page"].search(from_airport, from_airport, start_date, end_date)

        assert_that(self.pages["results_page"].wait_for_search_completion()).is_true()

        expected_page_title = self.json_reader.read_from_json()["search"][
            "results_page_title"
        ]
        assert_that(expected_page_title).is_equal_to(
            self.pages["results_page"].get_title()
        )
        assert_that(self.pages["results_page"].results_shown()).is_true()

    @allure.title("Search for a rental being dropped off at a different location")
    @pytest.mark.parametrize(
        "from_airport, to_airport, start_date, end_date", search_criteria
    )
    @pytest.mark.run(order=2)
    def test_search_one_way(self, from_airport, to_airport, start_date, end_date):
        """Search with from and to airport being the same"""
        self.pages["home_page"].dismiss_warning()
        self.pages["home_page"].dismiss_email_subscription()
        self.pages["home_page"].search(from_airport, to_airport, start_date, end_date)

        assert_that(self.pages["results_page"].wait_for_search_completion()).is_true()

        expected_page_title = self.json_reader.read_from_json()["search"][
            "results_page_title"
        ]
        assert_that(expected_page_title).is_equal_to(
            self.pages["results_page"].get_title()
        )
        assert_that(self.pages["results_page"].results_shown()).is_true()
