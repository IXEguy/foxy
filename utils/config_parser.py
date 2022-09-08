"""
A module to help parse, read and write config files
"""

import os
import configparser
from globals import dir_global


class ConfigParserIni:
    """Parses ini files"""

    def __init__(self, ini_file):
        self.config = configparser.ConfigParser()
        self.file_path = os.path.join(dir_global.INI_CONFIGS_PATH, ini_file)
        self.config.read(self.file_path)

    def config_section_dict(self, section):
        """
        Returns ini file sections as dictionary
        :param section:
        :return: dict object containing parsed section
        """
        section_dict = {}
        section_keys = self.config.options(section)
        for key in section_keys:
            try:
                section_dict[key] = self.config.get(section, key)
            except Exception:
                print(f"exception found in {key}")
                section_dict[key] = None
        return section_dict


class AllureEnvironmentParser:
    """Writes environment variables into allure environment file"""

    def __init__(self, file_name):
        self.file_path = os.path.join(dir_global.ALLURE_RESULTS_PATH, file_name)

    def write_to_allure_env(self, dic):
        f = open(
            self.file_path, "w+"
        )  # opens environment.properties file - creates it if it does not exist
        for key in dic:
            f.write(key + "=" + dic[key] + "\n")  # Write values as key-value pairs
        f.close()
