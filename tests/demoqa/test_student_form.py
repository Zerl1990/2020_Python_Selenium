"""Test Demo Form"""
import os
import pytest
from common.webdriver_factory import create_driver_instance, ROOT_DIR
from pages.demoqa.practice_form import PracticeForm


STUDENTS_DATA = [
    ('Luis', 'Rivas', 'luis@gmail.com', 'Male', ['Maths']),
    ('Sofia', 'Valenzuela', 'sofia@gmail.com', 'Male', ['Computer Science']),
    ('Miguel', 'Perez', 'miguel@gmail.com', 'Female', ['Maths', 'Computer Science'])
]


@pytest.mark.parametrize("first_name, last_name, email, gender, subjects", STUDENTS_DATA)
def test_one(first_name, last_name, email, gender, subjects):
    """Test form"""
    driver = create_driver_instance('chrome')
    page = PracticeForm(driver, 2)
    page.open()
    page.wait_until_loaded()
    page.set_first_name(first_name)
    page.set_last_name(last_name)
    page.set_email(email)
    page.set_gender(gender)
    page.set_mobile('0123456789')
    page.set_date_of_birth('Dec 15 2020')
    for subject in subjects:
        page.set_subject(subject)
    page.set_hobbies('Sports')
    file_path = os.path.join(ROOT_DIR, '.gitignore')
    page.set_file(file_path)
    page.set_current_address('TEST ADDRESS')
    page.set_state('NCR')
    page.set_city('Delhi')
    confirmation_form = page.submit()
    confirmation_form.wait_until_loaded()
    info = confirmation_form.get_table_info()
    assert info['Student Name'] == f'{first_name} {last_name}', 'Confirmation name is not valid'
    confirmation_form.close()
    page.close()

