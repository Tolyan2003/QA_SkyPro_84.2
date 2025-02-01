from time import sleep
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LK_Page:
    @allure.step("Инициализация страницы ЛК")
    def __init__(self, driver) -> None:
        self.__driver = driver

    @allure.step("Перейти на страницу ЛК: {url}")
    def go_lk(self, url):
        self.__driver.get(url)
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name="Страница ЛК открыта",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Ввести имя: {f_name}")
    def enter_first_name(self, f_name):
        first_name_input = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="first-name-0"]')))
        first_name_input.click()
        first_name_input.send_keys(f_name)
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name=f"Введено имя: {f_name}",
            attachment_type=allure.attachment_type.PNG
        )
        sleep(2)

    @allure.step("Ввести фамилию: {l_name}")
    def enter_last_name(self, l_name):
        last_name_input = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="last-name-0"]')))
        last_name_input.click()
        last_name_input.send_keys(l_name)
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name=f"Введена фамилия: {l_name}",
            attachment_type=allure.attachment_type.PNG
        )
        sleep(2)

    @allure.step("Ввести дату рождения: {date}")
    def enter_birth_date(self, date):
        birth_date_input = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.ID, "birth-date-0")))
        birth_date_input.click()
        date_str = f"{date.day:02d}.{date.month:02d}.{date.year}"
        birth_date_input.send_keys(date_str)
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name=f"Введена дата рождения: {date_str}",
            attachment_type=allure.attachment_type.PNG
        )
        sleep(2)

    @allure.step("Ввести номер документа: {document_number}")
    def enter_document_number(self, document_number):
        document_number_input = WebDriverWait(self.__driver, 10).until(
                EC.element_to_be_clickable((By.ID, "document-number-0")))
        document_number_input.click()
        document_number_input.send_keys(document_number)
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name=f"Введен номер документа: {document_number}",
            attachment_type=allure.attachment_type.PNG
        )
        sleep(2)

    @allure.step("Выбрать пол: Мужской")
    def radio_button_male(self):
        radio_button = self.__driver.find_element(By.CSS_SELECTOR, "input.s__F3DPfo8ByKD_b23V1xKZ[type='radio']")
        radio_button.click()
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name="Выбран пол: Мужской",
            attachment_type=allure.attachment_type.PNG
        )
        sleep(2)

    @allure.step("Нажать кнопку 'Добавить'")
    def enter_send(self):
        button = WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "button.s__dqLrjmV81lbY2ctpQQWt.s__WErm7_CLb_ylgTog3lrX.s__StP9lgSIqJnskicSyix1.s__f1UsosWbVEKg57lLhkEC.s__ceBrcQp1NVw3cf8D8Rmt.s__sdEoAzpqV_wSKBROCiMJ"))
        )
        button.click()
        allure.attach(
            self.__driver.get_screenshot_as_png(),
            name="Нажата кнопка 'Добавить'",
            attachment_type=allure.attachment_type.PNG
        )
        sleep(2)