# UI smoke cases: SauceDemo training store

| ID | Scenario | Expected result | Automation |
|---|---|---|---|
| UI-01 | Log in with the public standard training user | Inventory page opens and product heading is visible | Playwright |
| UI-02 | Add first product to cart | Cart contains the selected product | Playwright |
| UI-03 | Continue checkout with valid required fields | Overview shows payment information and selected product | Playwright |
| UI-04 | Finish checkout | Confirmation message is displayed | Playwright |

The automation uses only the public training account and test data. It does not interact with a real merchant or payment provider.
