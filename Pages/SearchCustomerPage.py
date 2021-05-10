import time
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Search_Customer_Page(BasePage):
    search_button_Css = (By.CSS_SELECTOR, "button[id='search-customers']")
    firstname_textbox_ID = (By.ID, "SearchFirstName")
    registered_user_entry_xpath = (By.XPATH,"//td[text()='James Pan']")
    month_dropdown_ID = (By.ID, "SearchMonthOfBirth")
    day_dropdown_ID = (By.ID, "SearchDayOfBirth")
    record_found_by_DOB_xpath = (By.XPATH,"//td[text()='Steve Gates']")

    def __init__(self, driver):
        self.driver = driver
        super(Search_Customer_Page, self).__init__(self.driver)

    def is_srch_button_visible(self):
        return self.is_visible(self.search_button_Css)

    def get_srch_page_title(self,title):
        return self.get_title(title)

    def enter_first_name(self,first_name):
        self.do_sendKeys(self.firstname_textbox_ID, first_name)

    def click_srch_button(self):
        self.do_click(self.search_button_Css)

    def is_registered_user_entry_available(self):
        return self.is_visible(self.registered_user_entry_xpath)

    def select_month_from_dropdown(self,index) :
        self.do_clear(self.firstname_textbox_ID)
        month = self.do_find_element(self.month_dropdown_ID)
        self.select_index_from_Select_dropdown(month,index)

    def select_day_from_dropdown(self,value):
        day = self.do_find_element(self.day_dropdown_ID)
        self.select_value_from_select_dropdown(day, value)

    def is_visible_record_found_by_DOB_xpath(self):
        return self.is_visible(self.record_found_by_DOB_xpath)
