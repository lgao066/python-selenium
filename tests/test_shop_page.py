from tests.base_test import BaseTest
from pages.home_page import *
from pages.cart_page import *


class TestShopPage(BaseTest):

    def test_4_purchase_products(self):
        ShopPage = HomePage(self.driver).click_shop_page()
        ShopPage.wait_element(*ShopPageLocators.PRODUCT1)
        ShopPage.buy_funny_cow()
        ShopPage.buy_funny_cow()
        ShopPage.buy_fluffy_bunny()
        CartPage = HomePage(self.driver).click_cart_page()
        CartPage.wait_element(*CartPageLocators.CHECKOUT)
        self.assertTrue(CartPage.check_fluffy_bunny(1) & CartPage.check_funny_cow(2))