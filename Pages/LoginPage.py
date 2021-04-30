from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from config.config import TestData
from Pages.HomePage import HomePage

class LoginPage(BasePage):

    username_text_id = (By.ID, "Email")
    password_text_id = (By.ID,"Password")
    login_button_css = (By.CSS_SELECTOR,"button[class*='login-button']")
    #log_out_link_linkText = (By.LINK_TEXT,"Logout")

    def __init__(self,driver):
        self.driver = driver
        super().__init__(self.driver)


    def get_login_page_title(self,title):
        return self.get_title(title)

    def clear_username(self):
        self.do_clear(self.username_text_id)

    def clear_password(self):
        self.do_clear(self.password_text_id)

    def enter_username(self,username):
        self.do_sendKeys(self.username_text_id,username)

    def enter_password(self,password):
        self.do_sendKeys(self.password_text_id,password)

    def click_login_button(self):
        self.do_click(self.login_button_css)

    def perform_login(self,username,password):
        self.clear_username()
        self.enter_username(username)
        self.clear_password()
        self.enter_password(password)
        self.click_login_button()
        return HomePage(self.driver)

    # def is_logout_visbile(self):
    #     return self.is_visible(self.log_out_link_linkText)







