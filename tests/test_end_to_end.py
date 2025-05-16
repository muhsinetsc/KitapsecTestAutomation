import pytest

from constants.account_page_locator import *
from constants.category_page_locator import *
from constants.home_page_locator import *
from constants.login_page_locator import *
from constants.my_basket_page_locator import *
from constants.my_favorites_page_locator import *
from constants.product_detail_page_locator import *
from constants.product_page_locator import *

from pages.account_page import AccountPage
from pages.base_page import BasePage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_basket_page import MyBasketPage
from pages.my_favorites_page import MyFavoritesPage
from pages.product_detail_page import ProductDetailPage
from pages.product_page import ProductPage

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestEndToEnd(BaseTest):

    def setup_method(self):
        self.base = BasePage(self.driver)
        self.home = HomePage(self.driver)
        self.login = LoginPage(self.driver)
        self.category = CategoryPage(self.driver)
        self.product = ProductPage(self.driver)
        self.detail = ProductDetailPage(self.driver)
        self.account = AccountPage(self.driver)
        self.my_basket = MyBasketPage(self.driver)
        self.my_favorites = MyFavoritesPage(self.driver)


    # Ürün arama işlemi
    def test_product_search(self):
        self.successful_login()
        
        # Arama kutusuna "Python" yazılır ve "ARA" butonuna tıklanarak arama işlemi gerçekleştirilir.
        self.home.product_search("Python")
        assert (click_search_button := self.base.wait_for_element_to_be_visible(CLICK_SEARCH_BUTTON)).text == "ARA", \
            f"Expected: 'ARA', but found: '{click_search_button.text}'"
        self.home.click_search_button()

        # Araması yapılan "Python" ürününün listelendiği doğrulanır.
        assert "Python" in (python_product_control := self.base.wait_for_element_to_be_visible(PYTHON_PRODUCT_CONTROL)).text == "Python", \
            f"Expected: 'Python', but found: {python_product_control}"


    # Sepete ürün ekleme işlemi
    def test_add_to_cart(self):
        self.successful_login()
        
        # "Kategoriler" seçeneğinin görüntülendiği doğrulanır ve "Kategoriler" seçeneğine tıklanır.
        assert (category_button := self.base.wait_for_element_to_be_visible(CATEGORY_BUTTON)).get_attribute("title") == "Kategoriler", \
            f"Expected title: 'Kategoriler', but found: '{category_button.get_attribute('title')}'"
        self.home.click_category_button_by_title("Kategoriler")

        # "Kategoriler" sayfasının açıldığı doğrulanır.
        assert self.base.wait_for_url_contains("tum-kategoriler/")

        # "YKS Kitapları" seçeneğinin görüntülendiği doğrulanır ve "YKS Kitapları" seçeneğine tıklanır.
        self.category.hover_over_yks_category()
        assert (yks_category_button := self.base.wait_for_element_to_be_visible(HOVER_OVER_YKS_CATEGORY)).text == "YKS Kitapları", \
            f"Expected: 'YKS Kitapları', but found: '{yks_category_button}'"
        self.category.click_yks_category()

        # "YKS Kitapları" sayfasının açıldığı doğrulanır.
        assert self.base.wait_for_exact_url("https://www.kitapsec.com/Products/YKS-Kitaplari/")
        
        # İkinci sayfaya gidilerek sayfanın açıldığı doğrulanır.
        assert (page_two := self.base.wait_for_element_to_be_visible(CLICK_PAGE_TWO)).text == "2", \
            f"Expected: '2', but found: '{page_two}'"
        self.product.click_page_two()
        assert self.base.wait_for_url_contains("2-6-0a0-0-0-0-0-0.xhtml")

        # Ürüne tıklanır ve ürün detay sayfasına gidildiği doğrulanır.
        self.product.hover_over_product()
        self.product.click_hover_over_product()
        self.detail.control_product_detail()
        self.base.wait_for_url_contains("/Products")
        
        # "Sepete Ekle" butonunun görüntülendiği doğrulanır ve "Sepete Ekle" butonuna tıklanır.
        assert (control_add_to_cart := self.base.wait_for_element_to_be_visible(CLICK_ADD_TO_CART)).text == "Sepete Ekle", \
            f"Expected: 'Sepete Ekle', but found: '{control_add_to_cart}'"
        self.detail.click_add_to_cart_button()

        # "Ürün başarılı bir şekilde sepete eklenmiştir." pop-up mesajının görüntülendiği doğrulanır.
        assert (added_to_cart := self.base.wait_for_element_to_be_visible(ADDED_TO_CART)).text == "Ürün başarılı bir şekilde sepete eklenmiştir.", \
            f"Expected: 'Ürün başarılı bir şekilde sepete eklenmiştir.', but found: '{added_to_cart}'"


    # Sepetten ürün silme işlemi
    def test_delete_from_to_art(self):
        self.successful_login()
        
        # "KPSS Kitapları" seçeneğinin görüntülendiği doğrulanır ve "KPSS Kitapları" seçeneğine tıklanır.
        assert (control_kpss_books_button := self.base.wait_for_element_to_be_visible(CLICK_KPSS_BOOKS_BUTTON)).get_attribute("title") == "KPSS Kitapları", \
            f"Expected title: 'KPSS Kitapları', but found: '{control_kpss_books_button.get_attribute('title')}'"
        self.home.click_kpss_books_button_title()

        # "KPSS Kitapları" sayfasının açıldığı doğrulanır.
        assert self.base.wait_for_exact_url("https://www.kitapsec.com/Products/KPSS-Kitaplari/")
        
        # Ürüne tıklanır ve ürün detay sayfasına gidildiği doğrulanır.
        self.product.click_kpss_product()
        self.base.wait_for_url_contains("/Products")

        # "Sepete Ekle" butonunun görüntülendiği doğrulanır ve "Sepete Ekle" butonuna tıklanır.
        assert (control_add_to_cart := self.base.wait_for_element_to_be_visible(CLICK_ADD_TO_CART)).text == "Sepete Ekle", \
            f"Expected: 'Sepete Ekle', but found: '{control_add_to_cart}'"
        self.detail.click_add_to_cart_button()

        # "Ürün başarılı bir şekilde sepete eklenmiştir." pop-up mesajının görüntülendiği doğrulanır.
        assert (added_to_cart := self.base.wait_for_element_to_be_visible(ADDED_TO_CART)).text == "Ürün başarılı bir şekilde sepete eklenmiştir.", \
            f"Expected: 'Ürün başarılı bir şekilde sepete eklenmiştir.', but found: '{added_to_cart}'"
        
        # "Sepetim" butonunun görüntülendiği doğrulanır ve "Sepetim" butonuna tıklanır.
        assert (control_my_basket_button := self.base.wait_for_element_to_be_visible(CLICK_MY_BASKET_BUTTON)).text == "Sepetim", \
            f"Expected: 'Sepetim', but found: '{control_my_basket_button}'"
        self.home.click_my_basket_button()
        
        # "Sepetim" sayfasının açıldığı doğrulanır.
        assert self.base.wait_for_url_contains("Sepetim.php")
        
        # Sepetin dolu olarak görüntülendiği doğrulanır ve "Sil" butonuna tıklanır.
        assert "Sil" in (control_delete_button := self.base.wait_for_element_to_be_visible(CLICK_DELETE_BUTTON).get_attribute("name")), \
            f"Expected 'Sil' in name, but got: '{control_delete_button}'"
        self.my_basket.click_delete_button()

        # Sepetin boş olarak görüntülendiği doğrulanır.
        assert (control_empty_basket := self.base.wait_for_element_to_be_visible(CONTROL_EMPTY_BASKET)).text == "Alışveriş sepetinizde ürün bulunmuyor", \
            f"Expected: 'Alışveriş sepetinizde ürün bulunmuyor', but found: '{control_empty_basket}'"


    # Favorilere ürün ekleme işlemi
    def test_add_to_favorites(self):
        self.successful_login()
        
        # "ÇOK SATANLAR" seçeneğinin görüntülendiği doğrulanır ve "ÇOK SATANLAR" seçeneğine tıklanır.
        assert (best_sellers_button := self.base.wait_for_element_to_be_visible(BEST_SELLERS_BUTTON)).get_attribute("title") == "ÇOK SATANLAR", \
            f"Expected title: 'ÇOK SATANLAR', but found: '{best_sellers_button.get_attribute('title')}'"
        self.home.click_best_sellers_button_title("ÇOK SATANLAR")

        # Ürüne tıklanır ve ürün detay sayfasına gidildiği doğrulanır.
        self.product.click_product_favorite()
        self.detail.control_product_detail()
        self.base.wait_for_url_contains("/Products")
                
        # "Favorilere Ekle" butonunun görüntülendiği doğrulanır ve "Favorilere Ekle" butonuna tıklanır.
        self.detail.hover_over_add_to_favorites_button()
        assert (control_product_detail := self.base.wait_for_element_to_be_visible(CONTROL_PRODUCT_DETAIL)).text == "❤ Favorilere Ekle", \
            f"Expected: '❤ Favorilere Ekle', but found: '{control_product_detail}'"
        self.detail.click_add_to_favorites_button()

        # "Ürün Favorilerinize Eklenmiştir." pop-up mesajının görüntülendiği doğrulanır.
        assert (added_to_favorites := self.base.wait_for_element_to_be_visible(ADDED_TO_FAVORITES)).text == "Ürün Favorilerinize Eklenmiştir.", \
            f"Expected: 'Ürün Favorilerinize Eklenmiştir.', but found: '{added_to_favorites}'"
        
        # "Tamam" butonunun görüntülendiği doğrulanır ve "Tamam" butonuna tıklanır.
        assert (okey_button := self.base.wait_for_element_to_be_visible(CLICK_OKEY_BUTTON)).text == "Tamam", \
            f"Expected: 'Tamam', but found: '{okey_button}'"
        self.login.click_okey_button()

        # "Favorilere Ekle" butonu metininin, tıklama sonrası "❤ Favorilerden Çıkar" olarak değiştiği doğrulanır.
        assert (remove_favorites := self.base.wait_for_element_to_be_visible(REMOVE_FAVORITES)).text == "❤ Favorilerden Çıkar", \
            f" Expected: '❤ Favorilerden Çıkar', but found: '{remove_favorites}'"


    # Favorilerden ürün silme işlemi
    def test_delete_from_favorites(self):
        self.successful_login()
        
        # "Favorilerim" butonunun görüntülendiği doğrulanır ve "Favorilerim" butonuna tıklanır.
        assert "Favorilerim" in (my_favorites_button := self.base.wait_for_element_to_be_visible(CLICK_MY_FAVORITES_BUTTON).get_attribute("href")), \
            f"Expected 'favoriler' in href, but got: '{my_favorites_button}'"
        self.account.click_my_favorites_button()

        # "Favorilerim" sayfasının açıldığı doğrulanır.
        assert self.base.wait_for_url_contains("?Git=Favorilerim")
        
        # "x" butonuna tıklayarak ürün favorilerden çıkartılır.
        self.my_favorites.click_remove_from_favori̇tes_button()

        # "Ürün Favorilerinizden Silinmiştir." pop-up mesajının görüntülendiği doğrulanır.
        assert (delete_in_favorites := self.base.wait_for_element_to_be_visible(DELETE_IN_FAVORITES)).text == "Ürün Favorilerinizden Silinmiştir.", \
            f"Expected: 'Ürün Favorilerinizden Silinmiştir.', but found: '{delete_in_favorites}'"
        
        # "Tamam" butonunun görüntülendiği doğrulanır ve "Tamam" butonuna tıklanır.
        assert (okey_button := self.base.wait_for_element_to_be_visible(CLICK_OKEY_BUTTON)).text == "Tamam", \
            f"Expected: 'Tamam', but found: '{okey_button}'"
        self.login.click_okey_button()
        
        # Favori listesinin boş olarak görüntülendiği doğrulanır.
        assert (control_empty_list := self.base.wait_for_element_to_be_visible(CONTROL_EMPTY_LIST)).text == "Listelenecek favori ürünleriniz bulunmuyor", \
            f"Expected: 'Listelenecek favori ürünleriniz bulunmuyor', but found: '{control_empty_list}'"