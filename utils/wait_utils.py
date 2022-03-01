from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class WaitUtils: 
    
    @staticmethod
    def wait_for_element_present(driver, element,  timeout):
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        return WebDriverWait(driver, timeout, ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((element)))
