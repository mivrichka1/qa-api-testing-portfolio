import os
import uuid

import pytest
import requests


BASE_URL = os.getenv("RESTFUL_BOOKER_URL", "https://restful-booker.herokuapp.com").rstrip("/")


@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    yield session
    session.close()


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def auth_token(api, base_url):
    response = api.post(
        f"{base_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=15,
    )
    assert response.status_code == 200, f"Auth failed: {response.status_code} {response.text}"
    token = response.json().get("token")
    assert token, "Auth response must include a token"
    return token


@pytest.fixture
def booking_payload():
    suffix = uuid.uuid4().hex[:8]
    return {
        "firstname": "QA",
        "lastname": f"Portfolio-{suffix}",
        "totalprice": 125,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-10-18", "checkout": "2026-10-20"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(api, base_url, auth_token, booking_payload):
    response = api.post(f"{base_url}/booking", json=booking_payload, timeout=15)
    assert response.status_code == 200, f"Create failed: {response.status_code} {response.text}"
    booking_id = response.json().get("bookingid")
    assert isinstance(booking_id, int), f"Expected integer bookingid, got {booking_id!r}"
    yield booking_id, booking_payload
    # Clean up only the record created by this test.
    api.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Cookie": f"token={auth_token}"},
        timeout=15,
    )
