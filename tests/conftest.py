"""
Common test related configurations. properties & methods.
"""
from datetime import datetime

import allure
import requests
from git import Repo
from pytest import fixture, hookimpl, mark
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from globals.dir_global import ROOT_DIR
from pages.main_page import MainPage
from pages.results_page import ResultsPage
from utils.config_parser import AllureEnvironmentParser
from utils.config_parser import ConfigParserIni


# reads parameters from pytest command line
def pytest_addoption(parser):
    """
    Add option to specify browser to run tests against
    :param parser:
    :return:
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser that the automation will run in",
    )


def get_public_ip():
    """
    Get the public IP to serve up allure reports.

    :return: IP address as string
    """
    return requests.get("http://checkip.amazonaws.com", timeout=60).text.rstrip()


@fixture(scope="session")
# instantiates ini file parses object
def properties() -> ConfigParserIni:
    """
    Read the values in props.ini and return it to the caller.
    :return: dictionary of config values
    """
    config_reader = ConfigParserIni("props.ini")
    return config_reader


@fixture(autouse=True, scope="session")
# fetch browser type and base url then writes a dictionary of key-value pair into allure's environment.properties file
def allure_env() -> None:
    """
    Prepare the environment.properties file for use with the Allure report.
    :return: None
    """
    yield
    repo = Repo(ROOT_DIR)
    env_parser = AllureEnvironmentParser("environment.properties")
    env_parser.write_to_allure_env(
        {
            "Browser": driver.name,
            "Driver_Version": driver.capabilities["browserVersion"],
            "Base_URL": base_url,
            "Commit_Date": datetime.fromtimestamp(
                repo.head.commit.committed_date
            ).strftime("%c"),
            "Commit_Author_Name": "RJ",  # repo.head.commit.author.name,
            "Branch": repo.active_branch.name,
        }
    )


# https://stackoverflow.com/a/61433141/4515129
@fixture
# Instantiates Page Objects
def pages() -> dict:
    """
    Return a list of locally defined page as a dict
    :return: locals as dict
    """
    home_page = MainPage(driver)
    results_page = ResultsPage(driver)
    return locals()


@fixture(autouse=True)
def create_driver(allure_env, properties, request):
    """
    Download and setup the browser driver specified for use with the current run.
    Driver Manager is used here, so that we no longer have to download the browser specific drivers manually

    :param allure_env:
    :param properties:
    :param request:
    :return:
    """
    global browser, base_url, driver
    browser = request.config.option.browser
    base_url = properties.config_section_dict("Base Url")["base_url"]

    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "chrome_headless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-web-security")
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options
        )
    driver.implicitly_wait(10)
    driver.get(base_url)
    yield
    try:
        if request.node.rep_call.failed:
            screenshot_name = "screenshot on failure: %s" % datetime.now().strftime(
                "%d/%m/%Y, %H:%M:%S"
            )
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                body=get_public_ip(),
                name="public ip address",
                attachment_type=allure.attachment_type.TEXT,
            )
    except Exception as ex:
        print(f"Ran into Exception: {ex}")
    finally:
        driver.quit()


@mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    """
    Generates the report for the pytest run
    """
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@fixture(scope="function", autouse=True)
def test_debug_log(request):
    """
    Add to debug log when a test setup or execution fails
    :param request:
    :return:
    """
    def test_result():
        if request.node.rep_setup.failed:
            print("setting up a test failed!", request.node.nodeid)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                print("executing test failed", request.node.nodeid)

    request.addfinalizer(test_result)


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Generates the report for the pytest run
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
