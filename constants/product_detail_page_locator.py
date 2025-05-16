from selenium.webdriver.common.by import By

CONTROL_PRODUCT_DETAIL             = (By.CSS_SELECTOR,"[class='btn fvekleBtn']")
CLICK_ADD_TO_CART                  = (By.CSS_SELECTOR,"[class='btnSepetEkle radius']")
CLICK_ADD_TO_CART_BUTTON           = (By.CSS_SELECTOR,"[class='btnSepetEkle radius']")
ADDED_TO_CART                      = (By.XPATH,"//*[contains(text(), 'Ürün başarılı bir şekilde sepete eklenmiştir.')]")
ADD_TO_FAVORITES_BUTTON            = (By.CSS_SELECTOR,"[class='btn fvekleBtn']")
ADDED_TO_FAVORITES                 = (By.CSS_SELECTOR,".showSweetAlert.sweet-alert.visible > p")
REMOVE_FAVORITES                   = (By.CSS_SELECTOR,"[class='btnred fvekleBtn']")