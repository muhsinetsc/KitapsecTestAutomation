import pytest
import allure
from pages.base_page import *
from constants.login_page_locator import *


@pytest.mark.usefixtures("setup")
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("'Email adresinizi yaziniz' alani doldurulur.")
    def email_input(self,email):
        self.send_keys_to_element(EMAIL_INPUT, email)
        self.shot()

    @allure.step("'Şifrenizi yaziniz' alani doldurulur.")
    def password_input(self,password):
        self.send_keys_to_element(PASSWORD_INPUT, password)
        self.shot()
    
    @allure.step("'Guvenlik Kodu Girin' alanina tiklanir.")
    def click_security_code(self):
        self.click_to_element(CLICK_SECURITY_CODE)
        self.shot()

    @allure.step("'Giris Yap' butonuna tiklanir.")
    def click_login_button(self):
        self.click_to_element(CLICK_LOGIN_BUTTON)
        self.shot()

    @allure.step("'Tamam' butonuna tiklanir.")
    def click_okey_button(self):
        self.click_to_element(CLICK_OKEY_BUTTON)
        self.shot()