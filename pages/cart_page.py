from pages.base_page import BasePage
from locators.locators import *

class CartPage(BasePage):
    def __init__(self, driver):
        self.locator = CartPageLocators
        super().__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.CHECKOUT) else False

    def check_funny_cow(self, num):
        item_num= int(self.find_element(*self.locator.NUM_FUNNY_COW).get_attribute("value"))
        return True if item_num==num else False

    def check_fluffy_bunny(self, num):
        item_num = int(self.find_element(*self.locator.NUM_FLUFFY_BUNNY).get_attribute("value"))
        return True if item_num==num else False