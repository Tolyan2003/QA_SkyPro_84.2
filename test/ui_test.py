from time import sleep
import allure
from selenium.webdriver.common.by import By
from datetime import datetime

from page.LK_Page import LK_Page
from page.Main_Page import MainPage
from settings import base_url_ui, url_auth, url_lk, origin_ui, destination_ui, first_name, last_name, number_doc, provider_ui
from page.AuthPage import AuthPage

@allure.epic("Авиасейлс - поиск дешевых билетов")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(url="https://www.aviasales.ru/", name="Авиасейлс")
class TestAviaSales:
    """
    Сервис Авиасейлс позволяет подобрать авиабилеты на разные направления и даты,
    при этом возможны различные варианты рейсов, как прямые, так и сложные маршруты.
    А так же выбрать билеты разной ценовой категории
    """

    @allure.title("Поиск авиабилетов Москва-Сочи на 01 октября 2025 года")
    def test_search_tickets_moscow_sochi(self, browser):
        departure_date = datetime(2025, 10, 1)
        main_page = MainPage(browser)

        with allure.step("Открываем браузер Chrome по адресу https://www.aviasales.ru"):
            main_page.open_page(base_url_ui)

        with allure.step("Вводим город отправления"):
            main_page.enter_origin_city(origin_ui)

        with allure.step("Ввод города назначения"):
            main_page.enter_destination_city(destination_ui)

        with allure.step("Выбор даты вылета"):
            main_page.select_departure_date(departure_date)

        with allure.step("Выбор 'обратно не нужен'"):
            main_page.click_no_return_needed()

        with allure.step("Нажать кнопку Найти билеты"):
            main_page.search_for_tickets()

        with allure.step("Вернуться назад на Авиасейлс"):
            browser.back()

        with allure.step('Делаем скриншот для контроля'):
            current_time = int(datetime.now().timestamp())
            filename = f"./QA_{browser.name}_{current_time}.png"
            browser.save_screenshot(filename)


    @allure.title("Авторизация в профиле с использованием Google_ID")
    def test_auth(self, browser):
        with allure.step("Инициализируем страницу авторизации"):
            auth = AuthPage(browser)

        with allure.step("Получаем провайдера и URL для авторизации из конфига"):
            provider = provider_ui
            url = url_auth

        with allure.step(f"Переходим на страницу авторизации через {provider}"):
            auth.go(url)

        with allure.step(f"Производим вход через {provider}"):
            auth.login_as(provider)


    @allure.title("Ввод данных для покупки билетов в ЛК")
    def test_doc_lk(self, browser):
        with allure.step("Инициализируем страницу авторизации"):
            doc_lk = LK_Page(browser)

        with allure.step("Получаем параметры для документов из конфига"):
            birth_date = datetime(1990, 11, 12)

        with allure.step("Открываем браузер на странице личного кабинета пользователя сервиса Авиасейлс"):
            browser.get(url_lk)  # Используем драйвер для открытия страницы
            sleep(50)

        with allure.step("Вводим данные для покупки билетов - негативный тест"):
            doc_lk.enter_first_name('Ivan')
            doc_lk.enter_last_name('Petrov')
            doc_lk.enter_birth_date(birth_date)
            doc_lk.enter_document_number('AAAA_BBBBBB')

        with allure.step("Делаем скриншот страницы"):
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        with allure.step("Вводим данные для покупки билетов - негативный тест"):
            doc_lk.enter_first_name('')
            doc_lk.enter_last_name('')
            doc_lk.enter_document_number('')

        with allure.step("Вводим данные для покупки билетов"):
            doc_lk.enter_first_name(first_name)
            doc_lk.enter_last_name(last_name)
            doc_lk.enter_birth_date(birth_date)
            doc_lk.enter_document_number(number_doc)

        with allure.step("Проверяем, что данные введены корректно"):
            FIRST_NAME = first_name.upper()
            LAST_NAME = last_name.upper()
            assert browser.find_element(By.ID, "first_name_0").get_attribute("value") == FIRST_NAME
            assert browser.find_element(By.ID, "last_name_0").get_attribute("value") == LAST_NAME

        with allure.step("Делаем скриншот страницы"):
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
        )

        with allure.step("Нажимаем радиокнопку 'М'"):
            doc_lk.radio_button_male()

        with allure.step(":Жмем кнопку 'Добавить'"):
            doc_lk.enter_send()