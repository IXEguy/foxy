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
        """
        Init method of JsonParser
        :param json_path: Path to local json file that gets set as a class variable
        """
        self.json_path = os.path.join(dir_global.DATA_FILES_PATH, json_path)

    def read_from_json(self):
        """
        Read from the JSON file that the class was initialized with
        :return: json file object
        """
        # read from file
        with open(self.json_path, 'r') as json_file:
            json_reader = json.load(json_file)
        return json_reader