import allure
from selenium.webdriver.common.by import By

from base.page_base import PageBase
from utils.wait_utils import WaitUtils

class HomePage(PageBase):

    ####################LOCATORS

    #left menu
    menu_solutions = (By.CSS_SELECTOR, ".Solutions")
    menu_about_us = (By.CSS_SELECTOR, ".leftmenu [href*=about]")
    menu_services = (By.CSS_SELECTOR, ".leftmenu [href*=services]")
    menu_products = (By.CSS_SELECTOR, ".leftmenu [href*=products]")
    menu_locations = (By.CSS_SELECTOR, ".leftmenu [href*=contacts]") 
    menu_locations = (By.CSS_SELECTOR, ".leftmenu [href*=admin]")

    #login
    login_username = (By.CSS_SELECTOR, "#loginPanel [name=username]")
    login_password = (By.CSS_SELECTOR, "#loginPanel [name=password]")
    login_button = (By.CSS_SELECTOR, "#loginPanel [value='Log In']")
    login_forgotLoginInfo = (By.CSS_SELECTOR, "#loginPanel [href*='lookup']")
    login_register = (By.CSS_SELECTOR, "#loginPanel [href*='register']")

    ####################


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Getting title of the page")
    def get_page_title(self):
        return self.driver.title

    @allure.step("Login user")
    def login_user(self, username, password):
        self.driver.find_element(*self.login_username).send_keys(username)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    @allure.step("Go to Forget Login Info Page")
    def go_to_forget_login_info_page(self):
        self.driver.find_element(*self.login_forgotLoginInfo).click()

    @allure.step("Go to Register Page")
    def go_to_register_page(self):
        WaitUtils.wait_for_element_present(self.driver, self.driver.find_element(*self.login_register), 10)
        self.driver.find_element(*self.login_register).click()