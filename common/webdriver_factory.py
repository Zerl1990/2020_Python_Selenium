"""Factory to create new instance of web driver."""
import os
from selenium import webdriver
from selenium.webdriver.remote.file_detector import LocalFileDetector


__COMMON_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(__COMMON_DIR)
__CHROME_PATH = os.path.join(ROOT_DIR, 'drivers', 'chromedriver.exe')
__FIREFOX_PATH = os.path.join(ROOT_DIR, 'drivers', 'geckodriver.exe')


def create_driver_instance(browser_name: str):
    """Create a new web driver instance.

    :param browser_name: Browser name (chrome|firefox)
    :return: New web driver instance
    """
    if browser_name.lower() == 'chrome':
        chrome_opt = __create_chrome_options()
        return webdriver.Chrome(executable_path=__CHROME_PATH, chrome_options=chrome_opt)
    elif browser_name.lower() == 'firefox':
        firefox_driver = webdriver.Firefox(executable_path=__FIREFOX_PATH)
        firefox_driver.maximize_window()
        return firefox_driver
    elif browser_name.lower() == 'chrome-remote':
        options = webdriver.ChromeOptions()
        driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', options.to_capabilities())
        driver.file_detector = LocalFileDetector()
        return driver
    else:
        raise ValueError(f'Invalid browser selected: {browser_name}!')


def __create_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    return options


