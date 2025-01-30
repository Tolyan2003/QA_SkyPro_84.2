import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from page.Api_Page import ApiPage
from settings import timeout, browser_name


@pytest.fixture(scope='session')
def browser():
    """Фикстура для инициализации и завершения работы браузера."""



    #
    # with allure.step("Закрыть браузер"):
    #     try:
    #         driver.quit()
    #     except Exception as e:
    #         allure.attach(
    #             f"Ошибка при закрытии браузера: {str(e)}",
    #             name="Ошибка",
    #             attachment_type=allure.attachment_type.TEXT
    #         )
    #         pytest.fail(f"Ошибка при закрытии браузера: {str(e)}")

    with allure.step("Открыть и настроить браузер"):
        if browser_name == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        elif browser_name == "edge":
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)

        driver.implicitly_wait(timeout)
        driver.maximize_window()
        yield driver

    with allure.step("Закрыть браузер"):
        driver.quit()

@pytest.fixture(scope="module")
def api_page_object():
    """Фикстура для инициализации объекта ApiPage."""
    with allure.step("Инициализировать объект ApiPage"):
        return ApiPage()