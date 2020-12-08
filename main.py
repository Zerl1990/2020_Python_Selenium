"""Test classes"""
from common.webdriver_factory import create_driver_instance
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


try:
    driver = create_driver_instance('chrome-remote')
    driver.get('https://demoqa.com/books')
    wait = WebDriverWait(driver, 20)
    elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='rt-tr-group']")))
    for index, element in enumerate(elements):
        print(f'Row: {index}')
        sub_elements = element.find_elements_by_class_name('rt-td')
        print(f'\tTitle: {sub_elements[1].text}')
        print(f'\tAuthor: {sub_elements[2].text}')
        print(f'\tPublisher: {sub_elements[3].text}')
finally:
    driver.quit()
