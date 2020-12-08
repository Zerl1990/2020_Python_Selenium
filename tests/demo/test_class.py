# Define test case with class
import pytest
from common.webdriver_factory import create_driver_instance


@pytest.mark.e2e
class TestClass:
    def setup_method(self):
        """Setup method information"""
        self.driver = create_driver_instance('chrome')

    def teardown_method(self, method):
        """Tear down setup"""
        self.driver.close()

    def test_home_page(self):
        self.driver.get('http://google.com')
