import pytest
import allure
from pages.base_page import *
from constants.category_page_locator import *

@pytest.mark.usefixtures("setup")
class CategoryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("'YKS Kitaplari' secenegine gidilir.")
    def hover_over_yks_category(self):
        self.hover_over_element(HOVER_OVER_YKS_CATEGORY)
        self.shot()

    @allure.step("'YKS Kitaplari' secenegine tiklanir.")
    def click_yks_category(self):
        self.click_to_element(HOVER_OVER_YKS_CATEGORY)
        self.shot()