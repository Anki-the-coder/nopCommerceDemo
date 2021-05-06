import time
from Tests.test_Base import BaseTest
from Pages.LoginPage import LoginPage
from config.config import TestData
from utilities.logger import logGen


class Test_login(BaseTest):
    log = logGen.log()

    def test_verify_login_page_title(self):
        login = LoginPage(self.driver)
        self.log.info("Verifying Title of Login Page")
        final_title = login.get_login_page_title(TestData.Login_page_title)
        assert final_title == TestData.Login_page_title , self.log.error("Title of login page is different")
        self.log.info("Title of login page verified")


    def test_verify_login(self):
        login = LoginPage(self.driver)
        Home  = login.perform_login(TestData.User_name,TestData.Password)
        #time.sleep(2)


        #Using assert and Login Page class object
        # logout = login.is_logout_visbile()
        # assert logout ,"Login Failed"

        # Using If else and Login Page Class object
        # if not logout :
        #     print("login failed")
        # else :
        #     print("Login Successful")

        #using if else and Home Page Class obj
        #Home = HomePage(self.driver)

        # if Home.is_visible_logout_link() :
        #     print("pass")
        # else:
        #     print("fail")

        #Using Assert and Home page Cls obj
        ele = Home.is_visible_logout_link()
        assert ele

