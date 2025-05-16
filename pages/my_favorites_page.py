import pytest
import allure
from pages.base_page import *
from constants.my_favorites_page_locator import *


@pytest.mark.usefixtures("setup")
class MyFavoritesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("'x' butonuna tiklanir.")
    def click_remove_from_favori̇tes_button(self):
        self.click_to_element(CLICK_REMOVE_FROM_FAVORITES_BUTTON)
        self.shot()