import pytest
import json
from pathlib import Path
from jsonschema import validate


pytestmark = pytest.mark.api
BOOKING_SCHEMA = json.loads((Path(__file__).parent.parent / "schemas" / "booking.schema.json").read_text())


def test_booking_list_returns_ids(api, base_url):
    response = api.get(f"{base_url}/booking", timeout=15)
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert all(isinstance(item.get("bookingid"), int) for item in body)


def test_get_created_booking_matches_payload(api, base_url, created_booking):
    booking_id, payload = created_booking
    response = api.get(f"{base_url}/booking/{booking_id}", timeout=15)
    assert response.status_code == 200
    body = response.json()
    validate(instance=body, schema=BOOKING_SCHEMA)
    assert body == payload


@pytest.mark.parametrize("booking_id", [0, "not-a-number"])
def test_invalid_booking_id_is_rejected(api, base_url, booking_id):
    response = api.get(f"{base_url}/booking/{booking_id}", timeout=15)
    assert response.status_code == 404


def test_update_without_auth_is_rejected(api, base_url, created_booking):
    booking_id, payload = created_booking
    response = api.put(f"{base_url}/booking/{booking_id}", json=payload, timeout=15)
    assert response.status_code in (401, 403)


def test_authorized_update_changes_booking(api, base_url, auth_token, created_booking):
    booking_id, payload = created_booking
    updated = {**payload, "firstname": "QA-Updated", "totalprice": 150}
    response = api.put(
        f"{base_url}/booking/{booking_id}",
        json=updated,
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
    assert response.status_code == 200
    assert response.json()["firstname"] == "QA-Updated"
    assert response.json()["totalprice"] == 150


def test_create_boundary_values(api, base_url, auth_token):
    payload = {
        "firstname": "Boundary",
        "lastname": "Case",
        "totalprice": 0,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-10-18", "checkout": "2026-10-18"},
        "additionalneeds": "",
    }
    response = api.post(f"{base_url}/booking", json=payload, timeout=15)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    try:
        created = api.get(f"{base_url}/booking/{booking_id}", timeout=15)
        assert created.status_code == 200
        assert created.json()["totalprice"] == 0
        assert created.json()["additionalneeds"] == ""
    finally:
        api.delete(
            f"{base_url}/booking/{booking_id}",
            headers={"Cookie": f"token={auth_token}"},
            timeout=15,
        )


def test_delete_without_auth_is_rejected(api, base_url, created_booking):
    booking_id, _ = created_booking
    response = api.delete(f"{base_url}/booking/{booking_id}", timeout=15)
    assert response.status_code in (401, 403)


def test_delete_created_booking_and_verify_absence(api, base_url, auth_token, created_booking):
    booking_id, _ = created_booking
    response = api.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
    assert response.status_code in (200, 201)
    check = api.get(f"{base_url}/booking/{booking_id}", timeout=15)
    assert check.status_code == 404
