# Портфолио QA: API и UI-тестирование

[![Статус проверок](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml/badge.svg)](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml) · [Все запуски и отчёты GitHub Actions](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml)

Учебный проект с примерами тестирования REST API и веб-приложения: Postman/Newman, Python + pytest, Playwright, SQL и GitHub Actions.

## Где лежат файлы

В корне репозитория доступны исходники Python API-тестов (api_tests/), UI smoke-теста (ui_tests/), JSON Schema (schemas/booking.schema.json) и файлы конфигурации. Полный запускаемый проект находится в архиве [qa-api-testing-portfolio-unified.zip](./qa-api-testing-portfolio-unified.zip), в папке qa-api-portfolio/ внутри архива. В архиве также находятся коллекция Postman, SQL-примеры, отчёты и конфигурация CI.

Workflow GitHub Actions запускает проверки из архива. Откройте страницу запусков выше, выберите последний запуск, чтобы увидеть статус проверок и скачать отчёты из раздела **Artifacts**.

## Что проверяю и какие навыки демонстрирую

- REST API: CRUD-сценарии, коды ответов, структура и типы JSON, авторизация, негативные случаи и граничные значения.
- Python/pytest: фикстуры, параметризация, проверка JSON Schema и очистка созданных тестом данных.
- Postman/Newman: последовательные запросы, передача токена и ID между шагами, проверки ответов и запуск коллекции из CI.
- UI/Playwright: smoke-сценарий от входа до завершения оформления заказа на учебном магазине SauceDemo.
- Тестовая документация: сценарии, тест-кейсы, исследовательские заметки и результаты проверки.
- SQL: примеры запросов для проверки согласованности заказов; они иллюстративные и не запускались на реальной базе.

Публичная документация коллекции Postman: [открыть коллекцию](https://documenter.getpostman.com/view/59042488/2sBYHSxg8z).

## Запуск проекта

Требуются Python 3.12+, Node.js 22+, pnpm 11 и Chromium для UI-проверки. Для полного запуска распакуйте архив и выполните команды из папки qa-api-portfolio/:

~~~bash
unzip qa-api-testing-portfolio-unified.zip
cd qa-api-portfolio
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

Чтобы посмотреть коллекцию вручную, импортируйте postman/restful-booker.collection.json из распакованного проекта в Postman. Файл окружения можно импортировать отдельно.

## Ограничения

Проверки обращаются к публичным учебным сервисам, поэтому результат зависит от их доступности и текущего поведения. Тесты API удаляют созданные ими записи. SQL-примеры не выполняются против базы магазина. Описанные ответы Restful Booker относятся к учебному API, а не к промышленным системам.
