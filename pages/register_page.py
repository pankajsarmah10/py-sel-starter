import allure
from selenium.webdriver.common.by import By
from base.page_base import PageBase


class Register(PageBase):
    
    
    ####################LOCATORS

    register_first_name = (By.CSS_SELECTOR, "[id='customer.firstName']")
    register_last_name = (By.CSS_SELECTOR, "[id='customer.lastName']")
    register_address = (By.CSS_SELECTOR, "[id='customer.address.street']")
    register_city = (By.CSS_SELECTOR, "[id='customer.address.city']")
    register_state = (By.CSS_SELECTOR, "[id='customer.address.state']")
    register_zip_code = (By.CSS_SELECTOR, "[id='customer.address.zipCode']")
    register_phone_number = (By.CSS_SELECTOR, "[id='customer.phoneNumber']")
    register_ssn = (By.CSS_SELECTOR, "[id='customer.ssn']")

    register_username = (By.CSS_SELECTOR, "[id='customer.username']")
    register_password = (By.CSS_SELECTOR, "[id='customer.password']")
    register_confirm_password = (By.CSS_SELECTOR, "[id='repeatedPassword']")
    register_button = (By.CSS_SELECTOR, "#customerForm [value=Register] ")

    ####################

    def __init__(self, driver) -> None:
        super().__init__(driver)

    

    @allure.step("Register new user")
    def register_new_user(self, firstName, lastName, address, city, state, zipCode, phone, ssn, username, password):
        if firstName: self.driver.find_element(*self.register_first_name).sendKeys(firstName)
        if lastName: self.driver.find_element(*self.register_last_name).sendKeys(lastName)
        if address: self.driver.find_element(*self.register_address).sendKeys(address)
        if city: self.driver.find_element(*self.register_city).sendKeys(city)
        if state: self.driver.find_element(*self.register_state).sendKeys(state)
        if zipCode: self.driver.find_element(*self.register_zip_code).sendKeys(zipCode)
        if phone: self.driver.find_element(*self.register_phone_number).sendKeys(phone)
        if ssn: self.driver.find_element(*self.register_ssn).sendKeys(ssn)
        if username: self.driver.find_element(*self.register_username).sendKeys(username)
        if password: self.driver.find_element(*self.register_password).sendKeys(password)
        if password: self.driver.find_element(*self.register_confirm_password).sendKeys(password)
        self.driver.find_element(*self.register_button).click()