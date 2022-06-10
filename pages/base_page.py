from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data.base_url import base_url


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, base_url=base_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        try: 
            ele = self.driver.find_element(*locator)
        except:
            return False
        else:
            return ele

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait(self):
        WebDriverWait(self.driver, 1)

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def wait_no_element(self, *locator):
        try:
            WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT STILL PRESENT WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()