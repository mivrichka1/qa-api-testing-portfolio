# Портфолио QA: API и UI-тестирование

[![Статус проверок](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml/badge.svg)](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml) · [Все запуски и отчёты GitHub Actions](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml)

Учебный проект с ручными и автоматизированными проверками REST API и веб-приложения. Исходники разложены по папкам репозитория — скачивать ZIP для просмотра кода не нужно.

## Структура проекта

- api_tests/ — Python-тесты REST API на pytest: CRUD, авторизация, негативные и граничные сценарии.
- schemas/booking.schema.json — JSON Schema ответа API.
- postman/ — коллекция и окружение для Restful Booker; запуск через Newman.
- ui_tests/ — Playwright smoke-тест оформления заказа в SauceDemo.
- reports/ — тест-кейсы, сценарии UI, исследовательские заметки и результат проверки.
- sql/ — пример запросов для проверки согласованности заказов.
- .github/workflows/portfolio.yml — запуск проверок в GitHub Actions.

## Навыки и проверки

Проверяю коды ответов и структуру JSON, CRUD-сценарии, авторизацию, негативные случаи и граничные значения. В API-тестах использую фикстуры pytest, проверку JSON Schema и очистку созданных тестом данных. В Postman/Newman — последовательное выполнение запросов, передачу токена и ID между шагами. UI-тест проходит путь от входа до подтверждения заказа. CI запускает API, Postman/Newman и UI-проверки; отчёты доступны в Artifacts последнего запуска.

Публичная документация коллекции Postman: [открыть](https://documenter.getpostman.com/view/59042488/2sBYHSxg8z).

## Запуск

Требуются Python 3.12+, Node.js 22+, pnpm 11 и Chromium.

~~~bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pnpm install --frozen-lockfile
mkdir -p artifacts
~~~

Запуск проверок по отдельности:

~~~bash
python -m pytest api_tests -m api
pnpm test:postman
python -m pytest ui_tests -m ui
~~~

Коллекцию для ручного просмотра можно импортировать из postman/restful-booker.collection.json. ZIP в корне содержит архивную копию полного проекта.

## Ограничения

Проверки обращаются к публичным учебным сервисам, поэтому результат зависит от их доступности и текущего поведения. Тесты удаляют только созданные ими данные. SQL-файл содержит иллюстративные запросы и не запускался против реальной базы данных.
