from selenium.webdriver.common.by import By


class HomePageLocators(object):
    STARTSHOPPING = (By.XPATH, '//a[contains(.,"Shopping")]') 
    HOME = (By.ID, 'nav-home')
    SHOP = (By.ID, 'nav-shop')
    CONTACT = (By.ID, 'nav-contact')
    LOGIN = (By.ID, 'nav-login')
    CART = (By.ID, 'nav-cart')


class ContactPageLocators(object):
    FORENAME = (By.ID, 'forename')
    SURNAME = (By.ID, 'surname')
    EMAIL = (By.ID, 'email')
    TELEPHONE = (By.ID, 'telephone')
    MESSAGE = (By.ID, 'message')
    SUBMIT = (By.XPATH, '//a[.="Submit"]')
    BACK = (By.CSS_SELECTOR, 'a[ng-click="goBack()"]') 
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[class="alert alert-success"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div[class="alert-error"]')
    FORENAME_ERROR = (By.ID, 'forename-err')
    EMAIL_ERROR = (By.ID, 'email-err')
    MESSAGE_ERROR = (By.ID, 'message-err')
    TELEPHONE_ERROR = (By.ID, 'telephone-err')
    PROGRESS = (By.XPATH, '//div[@class="progress progress-info wait"]')


class ShopPageLocators(object):
    PRODUCT1 = (By.ID, 'product-1')
    BUY_FUNNY_COW = (By.XPATH, '//*[.="Funny Cow"]/..//a[contains(@class, btn)]')
    BUY_FLUFFY_BUNNY = (By.XPATH, '//*[.="Fluffy Bunny"]/..//a[contains(@class, btn)]')


class CartPageLocators(object):
    CHECKOUT = (By.XPATH, '//a[contains(.,"Check Out")]')
    ITEM_FUNNY_COW = (By.XPATH, '//tr[contains(.,"Funny Cow")]')
    NUM_FUNNY_COW = (By.XPATH, '//tr[contains(.,"Funny Cow")]//*[@type="number"]')
    ITEM_FLUFFY_BUNNY = (By.XPATH, '//tr[contains(.,"Fluffy Bunny")]')
    NUM_FLUFFY_BUNNY = (By.XPATH, '//tr[contains(.,"Fluffy Bunny")]//*[@type="number"]')


class LoginPageLocators(object):
    USERNAME = (By.ID, 'loginUserName')
    PASSWORD = (By.ID, 'loginPassword')
    LOGIN = (By.ID, '//*[contains(@class,"pop")]//button[.="Login"]')
    CANCEL = (By.ID, '//*[contains(@class,"pop")]//button[.="Cancel"]')
    ERROR_MESSAGE = (By.ID, 'login-error')