import pytest

from constants.home_page_locator import * 
from constants.login_page_locator import *

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    def setup_method(self):
        self.base = BasePage(self.driver)
        self.home = HomePage(self.driver)
        self.login = LoginPage(self.driver)

    # Sisteme başarılı giriş işlemi
    def test_success_login(self):
        # Ana sayfanın açıldığı doğrulanır.
        assert self.base.wait_for_exact_url("https://www.kitapsec.com/")

        # "Üye Girişi" butonunun görüntülendiği doğrulanır ve "Üye Girişi" butonuna tıklanır.
        assert (click_member_login_button := self.base.wait_for_element_to_be_visible(CLICK_MEMBER_LOGIN_BUTTON)).text == "Üye Girişi", \
            f"Expected: 'Üye Girişi', but found: '{click_member_login_button.text}'"
        self.home.click_member_login_button()
        
        # Üye girişi sayfasının açıldığı doğrulanır.
        assert (member_login_page_control := self.base.wait_for_element_to_be_visible(MEMBER_LOGIN_PAGE_CONTROL)).text == "Sitemize Üye Girişi Yaparak Siparişinizi Oluşturun", \
            f"Expected: 'Sitemize Üye Girişi Yaparak Siparişinizi Oluşturun', but found: '{member_login_page_control}'"

        # Kullanıcı bilgileri (email ve şifre) ilgili alanlara girilir.
        self.login.email_input(email)
        self.login.password_input(password)

        # "Güvenlik Kodu Girin" bilgisi girilir.
        self.login.click_security_code()
        self.base.wait_to_enter_the_security_code()

        # "Giriş Yap" butonunun görüntülendiği doğrulanır ve butona tıklanır. 
        assert (click_login_button := self.base.wait_for_element_to_be_visible(CLICK_LOGIN_BUTTON)).text == "Giriş Yap", f"Expected: 'Giriş Yap', but found: '{click_login_button.text}'"
        self.login.click_login_button()

        # "Tamam" butonunun görüntülendiği doğrulanır ve butona tıklanır.
        assert (click_okey_button := self.base.wait_for_element_to_be_visible(CLICK_OKEY_BUTTON)).text == "Tamam", f"Expected: 'Tamam', but found: '{click_okey_button.text}'"
        self.login.click_okey_button()

        # Başarılı giriş yapıldığı doğrulanır.
        assert self.base.wait_for_exact_url("https://www.kitapsec.com/Account.php")