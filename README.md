# QA portfolio project: API and UI checks

Portfolio project for a QA Intern / Junior QA application. It demonstrates API testing, basic UI regression, SQL data checks, test documentation, and CI configuration.

The complete source tree is available in the repository's `qa-api-portfolio.zip` archive; download and extract it to run the checks locally.

## What is included

- **Postman + Newman:** ordered Restful Booker CRUD flow with status/body assertions, auth token and booking ID variables, negative authorization checks, and cleanup of the booking created by the run.
- **Python + pytest + requests + JSON Schema:** API tests with fixtures, unique test data, parameterization, authorized/unauthorized cases, boundary values, response-schema validation, and cleanup.
- **Playwright:** UI smoke test for a training storefront: login, add a product to cart, proceed through checkout, and verify confirmation.
- **SQL:** example order-consistency checks in `sql/order_consistency_checks.sql`. These demonstrate validation queries for a conventional test schema; the public UI demo does not expose its database.
- **CI:** GitHub Actions workflow runs API, Postman, and UI suites and uploads HTML/JUnit reports.
- **Test cases and exploratory note:** `reports/test-cases.md` and `reports/exploratory-check.md`.
- **UI scenarios:** `reports/ui-test-cases.md`.

## Run locally

Python 3.12+, Node.js 22+, and Chromium are required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pnpm install --frozen-lockfile
mkdir -p artifacts
python -m pytest api_tests -m api --html=artifacts/api-report.html --self-contained-html --junitxml=artifacts/api-junit.xml
pnpm test:postman
python -m pytest ui_tests -m ui --html=artifacts/ui-report.html --self-contained-html --junitxml=artifacts/ui-junit.xml
```

The API suite creates and deletes only its own demo bookings. The UI suite uses SauceDemo's documented public training credentials (`standard_user` / `secret_sauce`) and places a test order in that training environment.

Override demo URLs if needed:

```bash
RESTFUL_BOOKER_URL=https://restful-booker.herokuapp.com python -m pytest api_tests -m api
UI_BASE_URL=https://www.saucedemo.com python -m pytest ui_tests -m ui
```

## Project boundaries

- Public demo services can be unavailable or rate-limited; a service outage is not automatically a product defect.
- SQL examples are illustrative because SauceDemo's database is not accessible to test users.
- The OWASP Juice Shop demo was checked on 2026-10-18 but returned an application error. No product bug was filed or claimed; details are recorded in `reports/exploratory-check.md`.
- The GitHub Actions workflow is ready in `.github/workflows/qa.yml`. It will run after this folder is pushed to a GitHub repository; it has not run on GitHub yet.
- The Postman export in this folder is a separate, importable enhanced collection based on the scenarios in the previously shared public documentation; it does not modify that published Postman page.

## Skills demonstrated

Postman, Newman, REST API, HTTP, JSON, Python, pytest, requests, Playwright, SQL, Git, GitHub Actions, test design, boundary-value testing, test data setup/cleanup, HTML and JUnit reports.
