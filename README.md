# QA_SkyPro_84.2

Данный проект явяется финальным в курсе иучения профессии тестировщика.
При выполнении проекта стояла задача автоматизации ручных тестов, созданных при выполнении курсовой работы по итогам первоой половины обучения.
Для изучения и создания тестов был использован сайт Авиасейлс.
В ходе выполнения проекта выявлено, что сайт сервиса Авиасейлсс предоставляет услуги множеству своих клиентов, соответсвенно использует огромное количеств персональных данных.
Вввиду этого, для защиты сайта и данных, используемых им, предоставляемых клиентами, используются меры защиты из-за чего создание автотестов имеет ряд сложностей.
При провдении тестирования сайта, используя методы REST API, стандартные HTTP-методы для выполнения операций с ресурсами. Основные методы REST API включают:
1. GET
Назначение: Получение данных или ресурса.
Использование: Запрос данных с сервера без изменения состояния ресурса.
Особенности:
Безопасный метод (не изменяет состояние ресурса).
Идемпотентный (повторные запросы дают одинаковый результат).
2. POST
Назначение: Создание нового ресурса или отправка данных на сервер.
Использование: Передача данных для создания нового ресурса или выполнения операции.
Особенности:
Небезопасный метод (изменяет состояние ресурса).
Неидемпотентный (повторные запросы могут создавать несколько ресурсов).
3. PUT
Назначение: Обновление или замена существующего ресурса.
Использование: Передача данных для полного обновления ресурса.
Особенности:
Небезопасный метод (изменяет состояние ресурса).
Идемпотентный (повторные запросы не изменяют результат).
4. PATCH
Назначение: Частичное обновление ресурса.
Использование: Передача данных для обновления только указанных полей ресурса.
Особенности:
Небезопасный метод (изменяет состояние ресурса).
Неидемпотентный (в зависимости от реализации).
5. DELETE
Назначение: Удаление ресурса.
Использование: Удаление указанного ресурса.
Особенности:
Небезопасный метод (изменяет состояние ресурса).
Идемпотентный (повторные запросы не изменяют результат).
Эти методы являются основой для работы с REST API и позволяют выполнять CRUD-операции (Create, Read, Update, Delete) с ресурсами.
Для проведения API тестирования на сайте Авиасейлс необходима регистрация на ресурсе и получение токена для работы с запросами. Применение API запросов позволяет получить раличную информацию.
UI-тестирование сайта Авиасейлс имеет определенные сложности из-за использууемых мер защиты. 

При составлении автотестов использован язык программирования Python и фреймворк pytest. Pytest — это популярный фреймворк для написания и запуска тестов в Python. Он предоставляет простой и мощный синтаксис для создания тестов, а также множество возможностей для их организации и выполнения. Так же для API-тестов использовалась библиотека requests.  Она предоставляет простой и удобный интерфейс для работы с HTTP-методами, такими как GET, POST, PUT, DELETE и другими. Библиотека requests устанавливается с помощью pip.
При создании UI-тестов использовался selenium, мощный инструмент для автоматизации веб-браузеров. Он позволяет имитировать действия пользователя, такие как клики, ввод текста, навигация по страницам и многое другое. Selenium широко используется для тестирования веб-приложений, парсинга данных и автоматизации рутинных задач.
В проекте паттерн Page Object, популярный паттерн проектирования, используемый в автоматизации тестирования веб-приложений. Он помогает сделать тесты более читаемыми, поддерживаемыми и масштабируемыми. Основная идея заключается в том, чтобы инкапсулировать логику взаимодействия с элементами страницы в отдельные классы (Page Objects), а тесты использовать для описания сценариев.
Тесты в проекте расположены в папке tests, а связанные страницы - в папке page. Используемые в коде фистулы, вынесены в отдельный файл, как и данные, используемые для тестирования. Для документирования применен фреймеворк allure,  фреймворк для создания визуально привлекательных и информативных отчетов о выполнении тестов. Он поддерживает множество языков программирования, включая Python, и интегрируется с популярными тестовыми фреймворками, такими как pytest, unittest и другими. Allure предоставляет детальную информацию о выполнении тестов, включая шаги, скриншоты, логи и метаданные.
Для запуска тестов используется команда pytest с указанием файла "pytest tests/ui_test.py".
Для полного запуска тестов написан скрипт run_test.sh