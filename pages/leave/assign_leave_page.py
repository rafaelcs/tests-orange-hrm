from pages.base.base_page import BasePage

from selenium.webdriver.common.by import By

class AssignLeavePage(BasePage):

    _assign_leave_button = (By.LINK_TEXT, 'Assign Leave')

    #assign leave form
    _employee_name_field = (By.ID, 'assignleave_txtEmployee_empName')
    _leave_type_dropdown = (By.ID, 'assignleave_txtLeaveType')
    _leave_balance_field = (By.ID, 'assignleave_leaveBalance')
    _from_date_field = (By.ID, 'assignleave_txtFromDate')
    _to_date_field = (By.ID, 'assignleave_txtToDate')
    _comment_field = (By.ID, 'assignleave_txtComment')

    def __init__(self, driver):
        super().__init__(driver)

    def access_assign_leave_page(self):
        '''Function to access assign leave page'''
        self.find_element(*self._assign_leave_button).click()
        self.wait_visibility_element(self._employee_name_field)

    def assign_leave(self, employee_name, leave_type, from_date, to_date, comment):
        '''Function to assign leave to any employee'''
        self.find_element(*self._employee_name_field).send_keys(employee_name)
        self.select_option(*self._leave_type_dropdown, leave_type)
        self.find_element(*self._from_date_field).send_keys(from_date)
        self.find_element(*self._to_date_field).send_keys(to_date)
        self.find_element(*self._comment_field).send_keys(comment)
        self.find_element(*self._assign_leave_button).click()
