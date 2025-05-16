import pytest
import allure
from pages.base_page import *
from constants.product_page_locator import *


@pytest.mark.usefixtures("setup")
class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Sayfa ikiye tiklanir.")
    def click_page_two(self):
        self.hover_over_element_click(CLICK_PAGE_TWO)
        self.shot()

    @allure.step("Urune gidilir.")
    def hover_over_product(self):
        self.hover_over_element(HOVER_OVER_PRODUCT)
        self.shot()

    @allure.step("Urune tiklanir.")
    def click_hover_over_product(self):
        self.wait_for_elements_to_be_visible(CLICK_PRODUCT)[12].click()
        self.shot()

    @allure.step("'KPSS Kitaplari' secenegine tiklanir.")
    def click_kpss_product(self):
        self.wait_for_elements_to_be_visible(CLICK_PRODUCT)[0].click()
        self.shot()
    
    @allure.step("Urune tiklanir.")
    def click_product_favorite(self):
        self.wait_for_elements_to_be_visible(CLICK_PRODUCT_FAVORITE)[0].click()
        self.shot()