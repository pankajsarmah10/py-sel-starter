from base.page_base import PageBase
from selenium.webdriver.common.by import By
import allure

class Overview(PageBase):

    ####################LOCATORS

    overview_menu_open_new_account = (By.CSS_SELECTOR, "[href*=openaccount]")
    overview_menu_accounts_overview = (By.CSS_SELECTOR, "[href*=overview]")
    overview_menu_transfer_funds = (By.CSS_SELECTOR, "[href*=transfer]")
    overview_menu_bill_pay = (By.CSS_SELECTOR, "[href*=billpay]")
    overview_menu_find_transactions = (By.CSS_SELECTOR, "[href*=findtrans]")
    overview_menu_update_contact_info = (By.CSS_SELECTOR, "[href*=updateprofile]")
    overview_menu_request_loan = (By.CSS_SELECTOR, "[href*=requestloan]")
    overview_menu_logout = (By.CSS_SELECTOR, "[href*=logout]")
    overview_welcome_message = (By.CSS_SELECTOR, ".title")
    
    ####################
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Logout")
    def logout(self):
        self.driver.find_element(*self.overview_menu_logout).click()