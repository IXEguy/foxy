"""
Base Test Class File
"""
import pytest

from utils.json_parser import JsonParser


class BaseTest:
    """
    Base Test class that forms the basis of our tests
    """
    pages = None
    json_reader = None
    config_reader = None

    @pytest.fixture(autouse=True)
    def injector(self, pages, properties):
        # instantiates pages object, and data readers
        self.pages = pages
        self.json_reader = JsonParser("test_data.json")
        self.config_reader = properties
        # self.excel_reader = ExcelParser("data.xls")
