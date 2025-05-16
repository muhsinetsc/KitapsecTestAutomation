from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os

# .env dosyasi yüklenir.
load_dotenv()
# .env dosyasindaki degiskenler alinir.
email                              = os.getenv('EMAIL')
password                           = os.getenv('PASSWORD')

EMAIL_INPUT                        = (By.ID,"floatingInput")
PASSWORD_INPUT                     = (By.ID,"floatingPassword")
CLICK_SECURITY_CODE                = (By.CSS_SELECTOR,"[name='Gkodu']")
CLICK_LOGIN_BUTTON                 = (By.CSS_SELECTOR,"[class='btn btn-danger btn-block fa-lg gradient-custom-2 mb-3']")
CLICK_OKEY_BUTTON                  = (By.CSS_SELECTOR,"[class='confirm']")