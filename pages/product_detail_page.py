import pytest
import allure
from pages.base_page import *
from constants.product_detail_page_locator import *


@pytest.mark.usefixtures("setup")
class ProductDetailPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Urun detayina gidilir.")
    def control_product_detail(self):
        self.hover_over_element(CONTROL_PRODUCT_DETAIL)
        self.shot()

    @allure.step("'Sepete Ekle' butonuna tiklanir.")
    def click_add_to_cart_button(self):
        self.click_to_element(CLICK_ADD_TO_CART_BUTTON)
        self.shot()

    @allure.step("'Favorilere Ekle' butonuna gidilir.")
    def hover_over_add_to_favorites_button(self):
        self.hover_over_element(ADD_TO_FAVORITES_BUTTON)
        self.shot()

    @allure.step("'Favorilere Ekle' butonuna tiklanir.")
    def click_add_to_favorites_button(self):
        self.click_to_element(ADD_TO_FAVORITES_BUTTON)
        self.shot()