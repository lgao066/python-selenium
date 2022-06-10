from pages.base_page import BasePage
from pages.shop_page import ShopPage
from pages.contact_page import ContactPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from locators.locators import *


class HomePage(BasePage):
    
    def __init__(self, driver):
        self.locator = HomePageLocators
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.STARTSHOPPING) else False

    def click_home_page(self):
        self.find_element(*self.locator.HOME).click()
        return self(self.driver)

    def click_shop_page(self):
        self.find_element(*self.locator.SHOP).click()
        return ShopPage(self.driver)

    def click_contact_page(self):
        self.find_element(*self.locator.CONTACT).click()
        return ContactPage(self.driver)

    def click_login_page(self):
        self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)

    def click_cart_page(self):
        self.find_element(*self.locator.CART).click()
        return CartPage(self.driver)