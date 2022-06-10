from pages.base_page import BasePage
from locators.locators import *


class ShopPage(BasePage):
    def __init__(self, driver):
        self.locator = ShopPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.PRODUCT1) else False

    def buy_funny_cow(self):
        self.find_element(*self.locator.BUY_FUNNY_COW).click()

    def buy_fluffy_bunny(self):
        self.find_element(*self.locator.BUY_FLUFFY_BUNNY).click()