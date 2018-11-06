from pages.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage(BasePage):

    _username_field = (By.ID, 'txtUsername')
    _password_field = (By.ID, 'txtPassword')
    _login_button = (By.ID, 'btnLogin')
    _welcome_button = (By.ID, 'welcome')
    
    def __init__(self, driver):
        super().__init__(driver)

    def fill_login_form(self, username, password):
        self.find_element(*self._username_field).send_keys(username)
        self.find_element(*self._password_field).send_keys(password)
        self.find_element(*self._login_button).click()
