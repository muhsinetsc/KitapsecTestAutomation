from selenium.webdriver.common.by import By

BASE_URL                           = "https://www.kitapsec.com/"

CLICK_MEMBER_LOGIN_BUTTON          = (By.CSS_SELECTOR,"a:nth-of-type(1) > .text")
MEMBER_LOGIN_PAGE_CONTROL          = (By.CSS_SELECTOR,"[class='dialogTitle']")
PRODUCT_SEARCH                     = (By.ID,"yeniAramaInput")
CLICK_SEARCH_BUTTON                = (By.CSS_SELECTOR,"[class='submitKs loadClick']")
PYTHON_PRODUCT_CONTROL             = (By.CSS_SELECTOR,"[class='Ks_ContentBlokTitle']")
CATEGORY_BUTTON                    = (By.CSS_SELECTOR,".link_menu_arama.black")
CLICK_KPSS_BOOKS_BUTTON            = (By.CSS_SELECTOR,"td:nth-of-type(2) > table a[title='KPSS Kitapları']")
CLICK_MY_BASKET_BUTTON             = (By.CSS_SELECTOR,"[class='text2']")
BEST_SELLERS_BUTTON                = (By.CSS_SELECTOR,".CokSatan")
CLICK_OKEY_BUTTON                  = (By.CSS_SELECTOR,"[class='confirm']")