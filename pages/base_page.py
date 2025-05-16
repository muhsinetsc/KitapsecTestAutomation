import inspect
import time
import os
import allure
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    
    def shot(self, name=None, save_to_disk=False, folder="screenshots"):
        name = name or inspect.stack()[1].function
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{name}_{timestamp}.png"
        image = self.driver.get_screenshot_as_png()

        # Allure'a ekle
        allure.attach(image, name=filename, attachment_type=allure.attachment_type.PNG)

        # Dosyaya kaydet
        if save_to_disk:
            os.makedirs(folder, exist_ok=True)
            with open(os.path.join(folder, filename), "wb") as f:
                f.write(image)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as error:
            raise AssertionError(f"[wait_for_element_to_be_visible] Element {locator} was not visible within {timeout} seconds.\nError: {str(error)}")
    
    def wait_for_elements_to_be_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except Exception as error:
            raise AssertionError(f"[wait_for_elements_to_be_visible] Elements with locator {locator} were not all visible within {timeout} seconds.\nError: {str(error)}")
    
    def wait_for_element_clickable(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except Exception as error:
            raise AssertionError(f"[wait_for_element_clickable] Element {locator} was not clickable within {timeout} seconds.\nError: {str(error)}")

    def wait_for_exact_url(self, url):
        try:
            return WebDriverWait(self.driver, 10).until(EC.url_to_be(url)) and self.driver.current_url
        except Exception as error:
            raise AssertionError(f"[wait_for_exact_url] The URL did not match the expected '{url}'.\nError: {str(error)}")
    
    def wait_for_url_contains(self, url, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.url_contains(url)) and self.driver.current_url
        except Exception as error:
            raise AssertionError(f"[wait_for_url_contains] The URL did not contain '{url}'.\nError: {str(error)}")
    
    def get_elements_by_title(self, locator, title_value):
        elements_title = self.wait_for_elements_to_be_visible(locator)
        for item in elements_title:
            if item.get_attribute("title") == title_value:
                return item
        return None  
    
    def hover_over_element(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_for_element_to_be_visible(locator)).perform()
    
    def hover_over_element_click(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_for_element_to_be_visible(locator)).click().perform()

    def send_keys_to_element(self, locator, text): 
        self.wait_for_element_to_be_visible(locator).clear()
        self.wait_for_element_to_be_visible(locator).send_keys(text)

    def wait_to_enter_the_security_code(self):
        time.sleep(10)

    def click_to_element(self, locator):
        self.wait_for_element_to_be_visible(locator).click()
    
    def click_to_clickable_element(self, locator):
        self.wait_for_element_clickable(locator).click()

    def click_elements_by_title(self, locator, title_value):
        self.get_elements_by_title(locator, title_value).click()