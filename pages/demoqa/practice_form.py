"""Abstract logic to control practice form"""
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PracticeForm(BasePage):
    """Practice form logic."""

    __URL = 'https://demoqa.com/automation-practice-form'

    __SUBMIT_LOC = (By.ID, 'submit')

    def __init__(self, driver: WebDriver, timeout: int = 20):
        super().__init__(driver, timeout, self.__URL)

    def wait_until_loaded(self):
        """Wait until body is loaded

        :return: None
        """
        self._wait.until(EC.visibility_of_element_located(self.__SUBMIT_LOC))
