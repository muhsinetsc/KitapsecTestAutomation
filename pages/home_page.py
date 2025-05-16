import pytest
import allure
from pages.base_page import *
from constants.home_page_locator import *


@pytest.mark.usefixtures("setup")
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("'Uye Girisi' butonuna tiklanir.")
    def click_member_login_button(self):
        self.click_to_element(CLICK_MEMBER_LOGIN_BUTTON)
        self.shot()

    @allure.step("Urun arama islemi: '{product_name}' aranir.")
    def product_search(self, product_name):
        self.send_keys_to_element(PRODUCT_SEARCH, product_name)
        self.shot()

    @allure.step("'ARA' butonuna tiklanir.")
    def click_search_button(self):
        self.click_to_element(CLICK_SEARCH_BUTTON)
        self.shot()

    @allure.step("'Kategoriler' butonuna tiklanir.")
    def click_category_button_by_title(self, title_value):
        self.click_elements_by_title(CATEGORY_BUTTON, title_value)
        self.shot()
        
    @allure.step("'KPSS Kitaplari' butonuna tiklanir.")
    def click_kpss_books_button_title(self):
        self.click_to_element(CLICK_KPSS_BOOKS_BUTTON)
        self.shot()

    @allure.step("'Sepetim' butonuna tiklanir.")
    def click_my_basket_button(self):
        self.click_to_clickable_element(CLICK_MY_BASKET_BUTTON)
        self.shot()

    @allure.step("'COK SATANLAR' butonuna tiklanir.")
    def click_best_sellers_button_title(self, title_value):
        self.click_elements_by_title(BEST_SELLERS_BUTTON, title_value)
        self.shot()