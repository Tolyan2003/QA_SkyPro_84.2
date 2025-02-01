#!/bin/bash

# Очистка предыдущих отчетов
rm -rf reports/allure_raw
rm -rf reports/allure_report

# Запуск тестов
pytest -v --browser=chrome --alluredir=allure-results/allure_raw

# Генерация отчета Allure
allure generate allure-results/allure_raw -o allure-results/allure_report --clean

# Открытие отчета в браузере
open allure-results/allure_report/index.html