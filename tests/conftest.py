import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants.home_page_locator import BASE_URL


@pytest.fixture(scope="function", autouse=True)
def setup(request):
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(BASE_URL)

    request.cls.driver = driver

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call): # Testim FAIL olursa allure raporuna otomatik olarak screenshot eklenir
    # pytest raporunu sarmalar ve sonuçları yakalar
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = getattr(item.cls, "driver", None)
        if driver:
            try:
                # Test adını al ve dosya ismi için düzenle
                test_name = item.name.replace(" ", "_")
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{test_name}_failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as error:
                print(f"Ekran görüntüsü alinamadi: {error}")