from selenium.webdriver.common.by import By
from Pages.SearchCustomerPage import Search_Customer_Page
from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage
from config.config import TestData
from Tests.test_Base import BaseTest
from config.SeachCustomerTestData import SearchCustomerTestData


class Test_SrchCust(BaseTest):

    def test_visibility_of_srch_button(self):
        login = LoginPage(self.driver)
        home = login.perform_login(TestData.User_name, TestData.Password)
        home.search_for(TestData.search_customers)
        home.press_enter_for_srch()
        srch_page = home.select_cust_option()
        srch_button = srch_page.is_srch_button_visible()
        assert srch_button, "Srch button not found"

    def test_verify_search_page_title(self):
        srch_page = Search_Customer_Page(self.driver)
        srch_page_title = srch_page.get_srch_page_title(SearchCustomerTestData.search_cust_title)
        assert srch_page_title == SearchCustomerTestData.search_cust_title, "Title is Different"

    def test_find_cust_by_first_name(self):
        srch_page = Search_Customer_Page(self.driver)
        srch_page.enter_first_name("james")
        srch_page.click_srch_button()
        flag = srch_page.is_registered_user_entry_available()
        assert flag, "Record not found"

    def test_find_cust_by_DOB(self):
        srch_page = Search_Customer_Page(self.driver)
        srch_page.select_month_from_dropdown(5)
        srch_page.select_day_from_dropdown("2")
        srch_page.click_srch_button()
        assert srch_page.is_visible_record_found_by_DOB_xpath() ,"Record not found"
        # print(record)
        # assert record, "Record not found"
