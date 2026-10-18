# QA Testing Portfolio

A single QA portfolio project combining API, UI, and database testing examples: Postman + Newman, Python + pytest, Playwright, SQL, and GitHub Actions.

## Project source

Download the complete runnable source tree, including the Postman collection, pytest suite, UI smoke test, SQL examples, reports, lockfile, and CI workflows: [qa-api-testing-portfolio-unified.zip](./qa-api-testing-portfolio-unified.zip). This archive consolidates the standalone Restful Booker project into this portfolio.

## Test coverage

- **Restful Booker API:** sequential auth and CRUD Postman flow; token and booking ID are passed automatically; response status, JSON fields, and data types are checked; unauthorized access, invalid IDs, required-field omission, malformed dates, and boundary values are covered. The flow removes only its own booking and verifies it is gone.
- **Python API suite:** pytest, requests, fixtures, JSON Schema, negative/unauthorized cases, boundary values, and cleanup.
- **UI smoke test:** Playwright login-to-checkout flow against the SauceDemo training storefront.
- **SQL examples:** illustrative order consistency queries for a conventional test schema.
- **CI:** GitHub Actions workflows run the API/Postman checks and UI suite and publish test reports as workflow artifacts.

Public Postman documentation: https://documenter.getpostman.com/view/59042488/2sBYHSxg8z

## Run locally

Requirements: Python 3.12+, Node.js 22+, pnpm, and Chromium for UI checks.

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

Import `postman/restful-booker.collection.json` into Postman to inspect or run the collection. The environment export is optional.

## Notes

These checks use public training services and depend on their availability and current demo credentials. SQL is illustrative because the storefront does not expose a database. Malformed-input behavior observed in the Restful Booker demo is documented as behavior of that demo API, not as a claim about production systems.
