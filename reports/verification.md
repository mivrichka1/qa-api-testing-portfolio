# Verification record

Checked on 2026-10-18 against the public demo endpoints.

- Python API suite: **9 passed**.
- Postman/Newman: **10 requests, 15 assertions, 0 failures**.
- UI Playwright suite: test is implemented and collected, but could not be executed in this macOS sandbox. Chromium launch was blocked by the host process policy (`bootstrap_check_in ... Permission denied`). The CI workflow runs this suite on GitHub Actions/Linux; it has not run there yet.
- OWASP Juice Shop demo: returned a Heroku application-error page; no application defect was confirmed. See `exploratory-check.md`.
