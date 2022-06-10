from tests.base_test import BaseTest
from pages.contact_page import *
from pages.home_page import *

class TestContactPage(BaseTest):

    def test_0_page_load(self):
        contactPage = HomePage(self.driver).click_contact_page()
        contactPage.wait_element(*ContactPageLocators.FORENAME)
        self.assertTrue(contactPage.check_page_loaded())

    def test_1_validate_errors_and_gone(self):
        contactPage = HomePage(self.driver).click_contact_page()
        contactPage.wait_element(*ContactPageLocators.SUBMIT)
        contactPage.click_submit_button()
        self.assertTrue(contactPage.check_forname_error_present()
        & contactPage.check_email_error_present()
        & contactPage.check_message_error_present())
        
        contactPage.enter_forename("test forname")
        contactPage.enter_email("test@test.com")
        contactPage.enter_message("test message")
        self.assertTrue((not contactPage.check_forname_error_present())
        & (not contactPage.check_email_error_present())
        & (not contactPage.check_message_error_present()))

    def test_2_successful_submission(self):
        contactPage = HomePage(self.driver).click_contact_page()
        contactPage.wait_element(*ContactPageLocators.FORENAME)
        contactPage.enter_forename("test forname")
        contactPage.enter_email("test@test.com")
        contactPage.enter_message("test message")
        contactPage.click_submit_button()
        contactPage.wait_no_element(*ContactPageLocators.PROGRESS)
        self.assertTrue(contactPage.check_sucessful_submission())

    def test_3_a_invalid_email(self):
        contactPage = HomePage(self.driver).click_contact_page()
        contactPage.wait_element(*ContactPageLocators.EMAIL)
        contactPage.enter_email("test@test") # Invalid email
        self.assertTrue(contactPage.check_email_error_present())

    def test_3_b_invalid_telephone(self):
        contactPage = HomePage(self.driver).click_contact_page()
        contactPage.wait_element(*ContactPageLocators.TELEPHONE)
        contactPage.enter_telephone("test") # Invalid telephone
        self.assertTrue(contactPage.check_telephone_error_present())
