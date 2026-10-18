# Test cases: RESTful Booker API

| ID | Scenario | Test data | Expected result | Automation |
|---|---|---|---|---|
| API-01 | Retrieve booking IDs | `GET /booking` | `200`; JSON array; each item has numeric `bookingid` | pytest, Postman |
| API-02 | Authenticate with demo credentials | valid demo user | `200`; non-empty token | pytest fixture, Postman |
| API-03 | Create booking | valid booking JSON | `200`; numeric ID returned | pytest, Postman |
| API-04 | Read created booking | ID saved from API-03 | `200`; response fields match submitted data | pytest, Postman |
| API-05 | Read nonexistent booking | ID `0` | `404` | pytest, Postman |
| API-06 | Update without authentication | created ID, no cookie | `401` or `403`; data not changed | pytest, Postman |
| API-07 | Update with authentication | created ID, token cookie | `200`; updated values returned | pytest |
| API-08 | Create boundary-value booking | price `0`, empty optional text | creation accepted and values retained | pytest |
| API-09 | Delete without authentication | created ID, no cookie | `401` or `403` | pytest, Postman |
| API-10 | Delete created booking | own ID and token | `200` or `201`; subsequent read is `404` | pytest, Postman |

Tests create unique records and clean up records they create. They do not delete existing demo data.
