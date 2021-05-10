from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendKeys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_find_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def get_element_text(self, by_locator):
        ele_txt = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele_txt.text

    def is_visible(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(ele)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def keyboard_actions(self, by_locator, action):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(action)

    @staticmethod
    def select_value_from_select_dropdown(dropdown, value):
        sel = Select(dropdown)
        sel.select_by_value(value)

    @staticmethod
    def select_index_from_Select_dropdown(dropdown, index):
        sel = Select(dropdown)
        sel.select_by_index(index)
