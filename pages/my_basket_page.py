import pytest
import allure
from pages.base_page import *
from constants.my_basket_page_locator import *


@pytest.mark.usefixtures("setup")
class MyBasketPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("'Sil' butonuna tiklanir.")
    def click_delete_button(self):
        self.click_to_element(CLICK_DELETE_BUTTON)
        self.shot()