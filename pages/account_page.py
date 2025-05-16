import pytest
import allure
from pages.base_page import *
from constants.account_page_locator import *

@pytest.mark.usefixtures("setup")
class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("'Favorilerim' butonuna tiklanir.")
    def click_my_favorites_button(self):
        self.click_to_element(CLICK_MY_FAVORITES_BUTTON)
        self.shot()