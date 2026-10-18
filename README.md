# Портфолио QA: API и UI-тестирование

[![Статус проверок](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml/badge.svg)](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml) · [Все запуски и отчёты CI](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml)

Учебный проект с ручными и автоматизированными проверками REST API и веб-магазина.

## Состав проекта

- `api_tests/` — pytest проверки RESTful Booker: CRUD, авторизация, негативные и граничные сценарии.
- `postman/` — коллекция и окружение Restful Booker; запуск через Newman.
- `schemas/booking.schema.json` — JSON Schema ответа API.
- `ui_tests/` — шесть pytest/Playwright сценариев SauceDemo: успешный заказ, неверный вход, три обязательных поля checkout, удаление товара. При падении UI-теста CI сохраняет screenshot и trace в артефактах.
- [`reports/shop-testing.md`](reports/shop-testing.md) — тест-план, чек-лист, кейсы, эквивалентные классы, границы, таблица решений, результаты исследовательского тестирования и баг-репорт SD-BUG-01.
- `sql/order_consistency_checks.sql` — примеры SELECT, JOIN, фильтрации и агрегатов для типовой схемы заказов.
- `.github/workflows/portfolio.yml` — GitHub Actions для API, Newman и UI suites.

## Результат исследовательской проверки

Выполнен учебный заказ: Sauce Labs Backpack за `$29.99`, налог `$2.40`, итог `$32.39`; страница показала “Thank you for your order!”. Это тестовая симуляция без реальной оплаты. Под `problem_user` воспроизводится одинаковая фотография собаки у карточек товаров; баг описан с областью действия и серьёзностью в отчёте. В короткой сессии под `standard_user` подтверждённых дефектов не найдено.

Интерактивный браузер не предоставил DevTools Network/HAR и логи Console. Поэтому сетевые запросы, статусы ответов и ошибки консоли не отмечены как проверенные. SQL использует отдельную иллюстративную учебную схему и никак не связан с базой SauceDemo; результаты запросов не сверяются с заказом в UI.

## Запуск

Требуются Python 3.12+, Node.js 22+, pnpm 11 и Chromium. Из корня репозитория:

~~~bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pnpm install --frozen-lockfile
mkdir -p artifacts
~~~

Запустить наборы отдельно:

~~~bash
python -m pytest api_tests -m api
pnpm test:postman
python -m pytest ui_tests -m ui
~~~

Отчёты HTML/JUnit и UI traces доступны в Artifacts последнего GitHub Actions запуска. Демо-сервисы могут быть недоступны или изменить поведение. Коллекция API: [Postman documentation](https://documenter.getpostman.com/view/59042488/2sBYHSxg8z).
