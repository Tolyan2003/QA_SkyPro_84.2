import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from settings import url_auth


class AuthPage:

    @allure.step("Инициация")
    def __init__(self, driver) -> None:
        self.url = url_auth
        self.__driver = driver

    @allure.step("Перейти на страницу авторизации")
    def go(self, url):
        self.__driver.get(url)

    @allure.step("Проверка авторизации через {provider}")
    def login_as(self, provider):
        try:
            auth_button = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, f"Войти через {provider}"))
            )
            auth_button.click()
        except TimeoutException:
            raise AssertionError(f"Элемент 'Войти через {provider}' не найден или не кликабелен.")