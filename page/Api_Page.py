import requests
import allure
from settings import base_url, token

@allure.epic("Авиасейлс - поиск дешевых билетов")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://www.aviasales.ru/", name="Авиасейлс")
class ApiPage:
    """
    Класс определяет сущность Travel, позволяющую поиск авиабилетов
    по различным критериям на сайте компании Авиасейлс.
    Результат запроса приходит в формате JSON, который обрабатывается
    """

    def __init__(self):
        self.base_url = base_url
        self.token = token
        self.headers = {'X-Access-Token': token}
        self.session = requests.Session()

    @allure.step("Запросить самый дешевый билет из {origin} в {destination} на дату {depart_date}")
    def get_cheap_prices(self, origin: str, destination: str, depart_date: str, return_date: str, page: int, currency: str):
        """Получает самые дешевые билеты."""
        params = {
            "origin": origin,
            "destination": destination,
            "depart_date": depart_date,
            "return_date": return_date,
            "page": page,
            "currency": currency
        }
        path = self.base_url + "/prices/cheap"
        response = requests.get(path, headers=self.headers, params=params)
        return response

    @allure.step("Поиск прямых рейсов из {origin} в {destination} на дату {depart_date}")
    def direct_tickets(self, origin: str, destination: str, depart_date: str, return_date: str):
        """Ищет прямые рейсы."""
        params = {
            "origin": origin,
            "destination": destination,
            "depart_date": depart_date,
            "return_date": return_date,
        }
        path = self.base_url + "/prices/direct"
        response = requests.get(path, headers=self.headers, params=params)
        return response

    @allure.step("Поиск билетов на каждый день из {origin} в {destination} на {depart_date}")
    def calendar_monthly_prices(self, origin: str, destination: str, depart_date: str, return_date: str, page: int, currency: str):
        """Ищет билеты на каждый день указанного месяца."""
        params = {
            "origin": origin,
            "destination": destination,
            "depart_date": depart_date,
            "calendar_type": None,
            "page": page,
            "currency": currency
        }
        path = self.base_url + "/prices/calendar"
        response = requests.get(path, headers=self.headers, params=params)
        return response


    @allure.step("Популярные маршруты авиакомпаний из {origin}")
    def city_directions(self, origin: str, currency: str):
        """Ищет билеты на каждый день указанного месяца."""
        params = {
            "origin": origin,
            "currency": currency
        }
        path = self.base_url + "/city-directions"
        response = requests.get(path, headers=self.headers, params=params)
        return response


    @allure.step("Популярные маршруты авиакомпаний")
    def airline_directions(self, airline_code: str, limit: str):
        """Ищет билеты на каждый день указанного месяца."""
        params = {
            "airline_code": airline_code,
            "limit": limit
        }
        path = self.base_url + "/airline-directions"
        response = requests.get(path, headers=self.headers, params=params)
        return response


    @allure.step("Самые дешевые билеты, сгруппированные по месяцам")
    def cheapest_tickets(self, origin: str, destination: str, currency: str):

        params = {
            "origin": origin,
            "destination": destination,
            "currency": currency
        }
        path = self.base_url + "/prices/monthly"
        response = requests.get(path, headers=self.headers, params=params)
        return response

