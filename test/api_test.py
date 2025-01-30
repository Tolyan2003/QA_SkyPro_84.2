import allure
from settings import currency, depart_date, destination, origin, page, return_date, airline_code, limit

@allure.id("QA_API_1")
@allure.story("Поиск самых дешевых билетов")
@allure.title("Положительный сценарий поиска билетов")
@allure.severity(allure.severity_level.NORMAL)
def test_search_cheapest_flights(api_page_object):
    response = api_page_object.get_cheap_prices(
        origin=origin,
        destination=destination,
        depart_date=depart_date,
        return_date=return_date,
        page=page,
        currency=currency
    )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, f"Ожидается статус-код 200, но получен {response.status_code}"

    with allure.step("Проверяем наличие 'success' в ответе"):
        assert "success" in response.text, "Ответ не содержит 'success'"

    with allure.step("Проверяем успешность в JSON-данных"):
        json_data = response.json()
        assert json_data["success"] is True, "JSON-данные не указывают на успех"


@allure.id("QA_API_1n1")
@allure.story("Негативный сценарий поиска билетов")
@allure.title("Неверный параметр 'origin'")
@allure.severity(allure.severity_level.MINOR)
def test_missing_origin_parameter(api_page_object):
    with allure.step("Отправляем запрос без параметра 'origin'"):
        response = api_page_object.get_cheap_prices(
            origin='WWW',
            destination=destination,
            depart_date=depart_date,
            return_date=return_date,
            page=1,
            currency=currency
        )
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 400, f"Ожидается статус-код 400, но получен {response.status_code}"

    with allure.step("Проверяем наличие ошибки в ответе"):
        assert "error" in response.text, "Ответ не содержит 'error'"

    with allure.step("Проверяем наличие ошибки в JSON-данных"):
        json_data = response.json()
        assert "error" in json_data, "JSON-данные не содержат 'error'"


@allure.id("QA_API_1n2")
@allure.story("Проверка ошибок")
@allure.title("Некорректный формат даты вылета")
@allure.severity(allure.severity_level.NORMAL)
def test_invalid_depart_date_format(api_page_object):
    response = api_page_object.get_cheap_prices(
        origin=origin,
        destination=destination,
        depart_date="invalid-date-format",
        return_date=return_date,
        page=1,
        currency=currency
    )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 400, f"Ожидается статус-код 400, но получен {response.status_code}"

    with allure.step("Проверяем наличие ошибки в ответе"):
        assert "error" in response.text, "Ответ не содержит 'error'"

    with allure.step("Проверяем наличие ошибки в JSON-данных"):
        json_data = response.json()
        assert "error" in json_data, "JSON-данные не содержат 'error'"


@allure.id("QA_API_2")
@allure.story("Поиск прямых рейсов")
@allure.title("Прямые рейсы из {origin} в {destination} на дату {depart_date}")
@allure.severity(allure.severity_level.NORMAL)
def test_direct_tickets(api_page_object):
    with allure.step(f"Проводим поиск прямых рейсов из {origin} в {destination} на дату {depart_date}"):
        response = api_page_object.direct_tickets(
            origin = origin,
            destination = destination,
            depart_date = depart_date,
            return_date = return_date,
        )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, f"Ожидаемый статус-код 200, полученный {response.status_code}"

    with allure.step("Проверяем наличие ключевых слов в ответе"):
        assert "flight_number" in response.text, "Ответ не содержит информацию о рейсах"


@allure.id("QA_API_2n")
@allure.story("Ошибка при поиске прямых рейсов")
@allure.title("Отсутствие параметра 'origin'")
@allure.severity(allure.severity_level.NORMAL)
def test_neg_direct_tickets_missing_origin(api_page_object):

    with allure.step(f"Попытка найти прямые рейсы без указания пункта отправления ({origin})"):
        response = api_page_object.direct_tickets(
            origin = None,
            destination = destination,
            depart_date = depart_date,
            return_date = return_date,
        )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 400, f"Ожидается статус-код 400, но получен {response.status_code}"

    with allure.step("Проверяем наличие сообщения об ошибке в ответе"):
        assert "Missing required parameter: origin" in response.text, "Ответ не содержит сообщения об ошибке"


@allure.id("QA_API_3")
@allure.story("Проверка билета на каждый день месяца")
@allure.title("Проверка статуса-кода ответа")
@allure.severity(allure.severity_level.NORMAL)
def test_calendar_monthly_prices(api_page_object):
    with allure.step("Запрашиваем цены на каждый день месяца"):
        response = api_page_object.calendar_monthly_prices(
            origin=origin,
            destination=destination,
            depart_date=depart_date,
            return_date=return_date,
            page=page,
            currency=currency
            )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, f"Ожидаемый статус-код 2xx, но получил {response.status_code}"

    with allure.step("Проверяем наличие номера рейса в ответе"):
        assert "flight_number" in response.text, "Ответ не содержит номер рейса"

    with allure.step("Проверяем значение success в ответе"):
        json_data = response.json()
        assert json_data['success'], "Значение success не равно True"


@allure.id("QA_API_3n")
@allure.story("Негативный тест. Проверка билета на каждый день месяца")
@allure.title("Код пункта назначения отсутствует в базе IATA")
@allure.severity(allure.severity_level.NORMAL)
def test_Neg_calendar_monthly_prices(api_page_object):
    with allure.step("Запрашиваем цены на каждый день месяца"):
        response = api_page_object.calendar_monthly_prices(
            origin=origin,
            destination='MRM',
            depart_date=depart_date,
            return_date=return_date,
            page=page,
            currency=currency
            )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 400, f"Ожидается статус-код 400, но получен {response.status_code}"

    with allure.step("Проверяем наличие ошибки в ответе"):
        assert "error" in response.text, "Ответ не содержит 'error'"


@allure.id("QA_API_4")
@allure.story("Проверка популярных направлений из города")
@allure.title("Проверка популярности направлений из Москвы")
@allure.severity(allure.severity_level.NORMAL)
def test_popular_routes_from_citi(api_page_object):
    with allure.step("Запрос направлений из Москвы"):
        response = api_page_object.city_directions(
            origin=origin,
            currency=currency
        )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, f"Ожидаемый статус-код 200, но получили {response.status_code}"

    with allure.step("Проверяем, что Москва указана как город отправления"):
        json_data = response.json()
        assert json_data["data"]["AER"]["origin"] == "MOW", "Город отправления указан как Москва"

    with allure.step("Проверяем, что в списке направлений присутствует хотя бы один маршрут"):
        assert len(json_data["data"]) > 0, "В списке направлений должен присутствовать хотя бы один маршрут"


@allure.id("QA_API_4n")
@allure.story("Проверка непопулярных маршрутов из Москвы")
@allure.title("Проверка редких маршрутов из Москвы")
@allure.severity(allure.severity_level.MINOR)
def test_neg_popular_routes_from_citi(api_page_object):
    with allure.step("Запрос направлений из Москвы"):
        response = api_page_object.city_directions(
            origin="GDX",
            currency=currency
        )

    with allure.step("Проверяем, что Москва указана как город отправления"):
        json_data = response.json()
        assert json_data["data"]["AER"]["origin"] != "MOW", "Город отправления не указан как Москва"

    with allure.step("Проверяем, что в списке направлений нет ни одного маршрута"):
        assert len(json_data["data"]) == 0, "В списке направлений нет ни одного маршрута"


@allure.id("QA_API_5")
@allure.story("Проверка популярных направлений авиакомпаний")
@allure.title("Проверка популярности направлений авиакомпании Аэрофлот (SU)")
@allure.severity(allure.severity_level.NORMAL)
def test_popular_routes_airline(api_page_object):
    with allure.step("Запрос направлений авиакомпании"):
        response = api_page_object.airline_directions(
            airline_code=airline_code,
            limit=limit
        )

    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, f"Ожидаемый статус-код 200, но получили {response.status_code}"

    with allure.step("Проверяем, что Москва указана как город отправления"):
        json_data = response.json()
        assert json_data["success"] == True, "Провеяем что значение success = True"

    with allure.step("Проверяем, что в списке направлений присутствует хотя бы один маршрут"):
        assert len(json_data["data"]) == 10, "Проверяем, что число выводимых маршрутов равно 10"


@allure.id("QA_API_5n")
@allure.story("Негативный тест. Проверка популярных направлений авиакомпаний")
@allure.title("Проверка популярности направлений авиакомпании 'FF'")
@allure.severity(allure.severity_level.NORMAL)
def test_neg_popular_routes_airlines(api_page_object):
    with allure.step("Запрос маршрутов авиакомпании 'FF'"):
        response = api_page_object.airline_directions(
            airline_code="FF",
            limit=limit
        )
        json_data = response.json()
    with allure.step("Проверяем статус-код ответа"):
        assert response.status_code == 200, f"Ожидается статус-код 200, но получен {response.status_code}"

    with allure.step("Проверяем, что в списке направлений маршруты отсутствуют"):
        assert len(json_data["data"]) == 0, "Проверяем, что число выводимых маршрутов равно 0"


@allure.id("QA_API_6")
@allure.story("Запрос самых дешевых билетов, сгруппированные по месяцам")
@allure.title("Проверка популярности направлений авиакомпании 'FF'")
@allure.severity(allure.severity_level.NORMAL)
def test_prices_monthly(api_page_object):
    with allure.step("Запрос самых дешевых билетов"):
        response = api_page_object.cheapest_tickets(
            origin=origin,
            destination=destination,
            currency=currency
            )
        json_data = response.json()
        with allure.step("Проверяем количество месяцев, выданных по запросу"):
            assert len(json_data["data"]) == 12, "Ожидалось 12 месяцев"

        with allure.step("Проверяем наличия в ответе '2025-12'"):
            assert json_data["data"]["2025-12"]

@allure.id("QA_API_6n")
@allure.story("Негативный тест. Запрос самых дешевых билетов, сгруппированные по месяцам")
@allure.title("Самые дешевые билеты, сгруппированные по месяцам")
@allure.severity(allure.severity_level.NORMAL)
def test_neg_prices_monthly(api_page_object):
    with allure.step("Запрос самых дешевых билетов"):
        response = api_page_object.cheapest_tickets(
            origin=origin,
            destination='Adler',
            currency=currency
            )
        json_data = response.json()
        with allure.step("Проверяем статус-код ответа"):
            assert response.status_code == 400, f"Ожидается статус-код 400, но получен {response.status_code}"

        with allure.step("Проверяем наличия в ответе '2025-12'"):
            assert json_data["success"] == False, "Провеяем что значение success = False"
