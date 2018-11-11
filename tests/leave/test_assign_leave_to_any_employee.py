from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.leave.assign_leave_page import AssignLeavePage
from data import login_data
from selenium import webdriver
import pytest

class TestAssignLeaveToEmployee:

    def setup_class(self):
        self.driver = webdriver.Firefox()
        self.base_page = BasePage(self.driver)
        self.login_page = LoginPage(self.driver)

    def test_login(self):
        self.base_page.visit()
        self.login_page.fill_login_form(**login_data.super_admin_credential)