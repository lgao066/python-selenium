from pages.base_page import BasePage
from locators.locators import *

class ContactPage(BasePage):
    def __init__(self, driver):
        self.locator = ContactPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.FORENAME) else False

    def check_forname_error_present(self):
        return True if self.find_element(*self.locator.FORENAME_ERROR) else False

    def check_email_error_present(self):
        return True if self.find_element(*self.locator.EMAIL_ERROR) else False

    def check_message_error_present(self):
        return True if self.find_element(*self.locator.MESSAGE_ERROR) else False

    def check_telephone_error_present(self):
        return True if self.find_element(*self.locator.TELEPHONE_ERROR) else False

    def check_sucessful_submission(self):
        return True if self.find_element(*self.locator.SUCCESS_MESSAGE) else False

    def enter_forename(self, forename):
        self.find_element(*self.locator.FORENAME).send_keys(forename)
        
    def enter_surname(self, surname):
        self.find_element(*self.locator.SURNAME).send_keys(surname)

    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)

    def enter_telephone(self, telephone):
        self.find_element(*self.locator.TELEPHONE).send_keys(telephone)

    def enter_message(self, message):
        self.find_element(*self.locator.MESSAGE).send_keys(message)

    def click_submit_button(self):
        self.find_element(*self.locator.SUBMIT).click()