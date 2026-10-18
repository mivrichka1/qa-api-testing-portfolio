# Exploratory check: public OWASP Juice Shop demo

- Date checked: 2026-10-18
- Project: [OWASP Juice Shop](https://github.com/juice-shop/juice-shop)
- Demo URL: <https://demo.owasp-juice.shop/>
- Observation: the demo endpoint returned a Heroku “Application Error” page instead of the application.
- Classification: environment/demo availability issue; this does not establish a defect in the Juice Shop application.
- Reproduction: open the demo URL in a browser.
- Result: application UI was unavailable during this check, so functional scenarios could not be tested.
- Reporting status: no issue submitted and no product bug claimed. Recheck the demo before filing anything.

The project README describes the linked demo as a deployment-test/sneak-peek instance. This report records only the observed availability failure and should not be presented as a confirmed application defect.
