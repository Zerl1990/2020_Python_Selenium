"""Run test cases for practice form."""
import os
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.practice_form import PracticeForm


driver = create_driver_instance('chrome')
try:
    page = PracticeForm(driver, 2)

    page.open()
    page.wait_until_loaded()

    page.set_first_name('Luis')
    print(f'First Name: {page.get_first_name()}')

    page.set_last_name('Rivas')
    print(f'Last Name: {page.get_last_name()}')

    page.set_email('luis.rivas.0606@gmail.com')
    print(f'Email: {page.get_email()}')

    page.set_gender('Female')
    print(f'Gender: {page.get_gender()}')

    page.set_mobile('0123456789')
    print(f'Mobile: {page.get_mobile()}')

    page.set_date_of_birth('Nov 30 2020')
    print(f'Date of Birth: {page.get_date_of_birth()}')

    page.set_subject('Maths')
    print(f'Subject: {page.get_subject()}')

    page.set_subject('Computer Science')
    print(f'Subject: {page.get_subject()}')

    page.set_hobbies('Sports')
    print(f'Hobbies: {page.get_hobbies()}')

    file_path = os.path.join(ROOT_DIR, '.gitignore')
    page.set_file(file_path)
    print(f'Selected file: {page.get_file()}')

    page.set_current_address('TEST ADDRESS')
    print(f'Address: {page.get_current_address()}')

    page.submit()
finally:
    driver.close()
