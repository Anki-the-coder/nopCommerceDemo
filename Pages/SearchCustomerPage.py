from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class Search_Customer_Page(BasePage):
    search_button_Css = (By.CSS_SELECTOR, "button[id='search-customers']")

    def __init__(self, driver):
        self.driver = driver
        super(Search_Customer_Page, self).__init__(self.driver)

    def is_srch_button_visible(self):
        return self.is_visible(self.search_button_Css)
