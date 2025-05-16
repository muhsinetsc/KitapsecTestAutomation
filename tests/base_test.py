from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage

from constants.login_page_locator import *

class BaseTest:

    def successful_login(self):
        base = BasePage(self.driver)
        home = HomePage(self.driver)
        login = LoginPage(self.driver)

        home.click_member_login_button()
        login.email_input(email)
        login.password_input(password)
        login.click_security_code()
        base.wait_to_enter_the_security_code()
        login.click_login_button()
        login.click_okey_button()