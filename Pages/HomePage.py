from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.SearchCustomerPage import Search_Customer_Page

class HomePage(BasePage) :
    logout_link_link_text = (By.LINK_TEXT,"Logout")
    search_textbox_css = (By.CSS_SELECTOR,"input[class*='admin-search-box']")
    customer_option_css = (By.XPATH,"//div[@id='user-selection'][1]")

    def __init__(self,driver):
        self.driver = driver
        super().__init__(self.driver)

    def is_visible_logout_link(self):
        return self.is_visible(self.logout_link_link_text)

    def get_Home_Page_title(self,title):
        return self.get_title(title)

    def search_for(self,search):
        self.do_sendKeys(self.search_textbox_css,search)

    def press_enter_for_srch(self):
        self.keyboard_actions(self.search_textbox_css,Keys.ENTER)

    def select_cust_option(self):
        self.do_click(self.customer_option_css)
        return Search_Customer_Page(self.driver)
