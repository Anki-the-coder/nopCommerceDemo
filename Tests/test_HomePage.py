import time

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
import pytest
from config.config import TestData
from Pages.SearchCustomerPage import Search_Customer_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("init_driver")
class Test_Home():

    def test_verify_homePage_title(self):
        login = LoginPage(self.driver)
        home = login.perform_login(TestData.User_name,TestData.Password)
        home_pageTitle = home.get_Home_Page_title(TestData.Home_page_title)
        assert home_pageTitle == TestData.Home_page_title

    def test_search_cust(self):
        home = HomePage(self.driver)
        home.search_for(TestData.search_customers)
        home.press_enter_for_srch()
        srch_cust = home.select_cust_option()
        assert srch_cust.is_srch_button_visible()
        print(srch_cust.is_srch_button_visible())
        #time.sleep(3)

