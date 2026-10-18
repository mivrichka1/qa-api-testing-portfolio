# QA Testing Portfolio

[![QA checks](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml/badge.svg)](https://github.com/mivrichka1/qa-api-testing-portfolio/actions/workflows/portfolio.yml)

API and UI testing examples using Postman/Newman, Python + pytest, Playwright, SQL, and GitHub Actions. The complete runnable source tree is available in the project archive below.

## Project source

Download and extract [`qa-api-testing-portfolio-unified.zip`](./qa-api-testing-portfolio-unified.zip). It contains the Postman collection, pytest API and UI suites, schema, SQL examples, test reports, and CI workflows.

## Coverage

- **REST API:** authenticated CRUD flow, response status and schema checks, unauthorized access, invalid IDs, malformed input, boundary values, and cleanup of test data.
- **Python API tests:** pytest, requests, fixtures, JSON Schema, negative cases, and cleanup.
- **UI smoke test:** Playwright login-to-checkout flow against the SauceDemo training storefront.
- **Test documentation:** test cases, exploratory notes, UI scenarios, and verification notes.
- **SQL:** illustrative order consistency queries for a conventional schema; these examples have not been run against a live database.
- **CI:** GitHub Actions runs API, Newman, and UI checks and publishes test reports as workflow artifacts.

Public Postman documentation: [view the collection](https://documenter.getpostman.com/view/59042488/2sBYHSxg8z).

## Run locally

Requirements: Python 3.12+, Node.js 22+, pnpm 11, and Chromium for UI checks.

```bash
unzip qa-api-testing-portfolio-unified.zip
cd qa-api-portfolio
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install chromium
pnpm install --frozen-lockfile
mkdir -p artifacts
```

Run checks independently:

```bash
python -m pytest api_tests -m api
pnpm test:postman
python -m pytest ui_tests -m ui
```

To inspect the API suite in Postman, import `postman/restful-booker.collection.json`; the exported environment is optional.

## Scope and limitations

The checks call public training services, so results depend on their availability and current demo behavior. SQL is illustrative because the storefront does not expose a database. Malformed-input behavior documented here describes the demo API only, not production systems.
