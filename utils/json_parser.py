"""
JSON parser utility for the project
"""
import json
import os
from globals import dir_global


class JsonParser:
    """
    Class to parse JSON files
    """

    def __init__(self, json_path):
        self.json_path = os.path.join(dir_global.DATA_FILES_PATH, json_path)

    def read_from_json(self):
        """
        Read from the JSON file that the class was initialized with
        :return: json file object
        """
        # read from file
        with open(self.json_path, "r", encoding="utf-8") as json_file:
            json_reader = json.load(json_file)
        return json_reader
