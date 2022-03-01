import pytest
import allure
from pages.home_page import HomePage
from pages.register_page import Register
from pages.overview_page import Overview

@pytest.mark.usefixtures("setup")
class TestRegistration:

    @allure.title("Register with valid data")
    @allure.description("This is a test for valid registration")
    def test_registration_passed(self):
        home_page = HomePage(self.driver)
        home_page.open()
        home_page.go_to_register_page()

        register_page = Register(self.driver)
        register_page.register_new_user('fn12345',
        'ln12345',
        'street1',
        'city',
        'state',
        '9876554',
        '9876567876',
        '98272726263533',
        'test_pankaj2',
        's3cret')
        overview_page = Overview(self.driver)
        welcome_message = "Welcome fn12345"
        assert welcome_message in self.driver.find_element(
            *Overview.overview_welcome_message  
        ).text
        overview_page.logout()
