"""Expedia home page"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page"""

    __URL = 'https://www.expedia.mx/'

    __LOGO_LOC = (By.XPATH, "//*[contains(@class, 'header-logo')]")

    __LIST_PROPERTY_LOC = (By.ID, 'listYourProperty')

    __SUPPORT_LOC = (By.ID, 'support-cs')

    __TRIPS_LOC = (By.ID, 'itinerary')

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, timeout, self.__URL)

    def wait_until_loaded(self):
        """Wait until page is loaded"""
        self._wait.until(EC.visibility_of_element_located(self.__LOGO_LOC))

    def click_logo(self):
        """Click logo"""
        self.__click_link(self.__LOGO_LOC)

    def list_property(self):
        """Click list property"""
        self.__click_link(self.__LIST_PROPERTY_LOC)

    def support(self):
        """Click support"""
        self.__click_link(self.__SUPPORT_LOC)

    def trips(self):
        """Click trips"""
        self.__click_link(self.__TRIPS_LOC)

    def __click_link(self, locator):
        element = self._wait.until(EC.element_to_be_clickable(locator))
        element.click()
