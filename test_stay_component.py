"""Test stay component logic."""
from common.webdriver_factory import create_driver_instance
from pages.expedia.home_page import HomePage

try:
    driver = create_driver_instance('chrome')
    expedia_hp = HomePage(driver)
    expedia_hp.open()
    expedia_hp.wait_until_loaded()
    expedia_hp.select_tab('stays')
    expedia_hp.stay.wait_until_loaded()
    expedia_hp.stay.destination.set_value('Mexico')
    calendar = expedia_hp.stay.click_check_in()
    print(f'First Month: {calendar.get_first_month()}')
    print(f'Second Month: {calendar.get_second_month()}')
    calendar.select_dates(20, 30)
    expedia_hp.stay.search()
finally:
    driver.close()


