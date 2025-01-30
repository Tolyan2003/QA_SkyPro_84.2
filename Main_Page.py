import allure
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser

    def _take_screenshot(self, name):
        """Делает скриншот и прикрепляет его к отчету Allure."""
        allure.attach(
            self.browser.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Открыть страницу {url}")
    def open_page(self, url):
        self.browser.get(url)
        self._take_screenshot("Страница открыта")

    @allure.step("Ввести город отправления: {city}")
    def enter_origin_city(self, city):
        origin_input = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-test-id="origin-input"]'))
        )
        origin_input.clear()
        origin_input.send_keys(city, Keys.RETURN)
        sleep(2)
        self._take_screenshot(f"Введен город отправления: {city}")
        assert origin_input.get_attribute("value") == city, f"Ожидаемый город: {city}, Фактический: {origin_input.get_attribute('value')}"

    @allure.step("Ввести город назначения: {city}")
    def enter_destination_city(self, city):
        destination_input = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-test-id="destination-input"]'))
        )
        destination_input.send_keys(city, Keys.RETURN)
        sleep(2)
        self._take_screenshot(f"Введен город назначения: {city}")
        assert destination_input.get_attribute("value") == city, f"Ожидаемый город: {city}, Фактический: {destination_input.get_attribute('value')}"

    @allure.step("Выбрать дату отправления: {date}")
    def select_departure_date(self, date):
        departure_date_input = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='start-date-field']"))
        )
        departure_date_input.send_keys(Keys.RETURN)
        sleep(5)
        self._take_screenshot("Открыт календарь выбора даты")

        departure_month_input = self.browser.find_element(By.XPATH, "//select[@data-test-id='select-month']")
        departure_month_input.click()
        sleep(2)
        self._take_screenshot("Открыт выбор месяца")

        month_option = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[@value='{date.year}-{date.month}']"))
        )
        month_option.click()
        sleep(2)
        self._take_screenshot(f"Выбран месяц: {date.month}")

        day_option = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@data-test-id='date-0{date.day}.{date.month}.{date.year}']"))
        )
        day_option.click()
        self._take_screenshot(f"Выбрана дата: {date.day}.{date.month}.{date.year}")

    @allure.step("Нажать на кнопку 'Обратный билет не нужен'")
    def click_no_return_needed(self):
        no_return_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='calendar-action-button']"))
        )
        no_return_button.click()
        self._take_screenshot("Нажата кнопка 'Обратный билет не нужен'")

    @allure.step("Начать поиск билетов")
    def search_for_tickets(self):
        submit_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@data-test-id="form-submit"]'))
        )
        submit_button.click()

        self._take_screenshot("Начало поиска билетов")
        # Проверка, что поиск начался (например, появление лоадера или результатов)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@data-test-id='search-results']"))
        )
        self._take_screenshot("Результаты поиска отображены")