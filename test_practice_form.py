from common.webdriver_factory import create_driver_instance
from pages.demoqa.practice_form import PracticeForm

driver = create_driver_instance('chrome')
page = PracticeForm(driver)
page.open()
page.wait_until_loaded()
page.close()