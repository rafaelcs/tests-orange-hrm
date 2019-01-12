from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def visit(self, base_url='https://opensource-demo.orangehrmlive.com/'):
        return self.driver.get(base_url)

    def is_element_visible(self, *locator):
        try:
            return self.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def get_text(self, *locator):
        """Return text from specific element"""
        return self.find_element(*locator).text

    def select_option(self, *locator, option):
        """Select visible text from a dropdown"""
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(option)

    def wait_visibility_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((locator)))

