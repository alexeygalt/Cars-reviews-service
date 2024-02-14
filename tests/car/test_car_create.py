import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_car(auth_client, manufacturer):
    response = auth_client.post(
        reverse("create_car"),
        data={
            "name": "Russia",
            "end_year": 2023,
            "start_year": 2020,
            "manufacturer": manufacturer.id,
        },
    )
    expected_response = {
        "id": response.data.get("id"),
        "name": response.data.get("name"),
        "end_year": 2023,
        "start_year": 2020,
        "manufacturer": manufacturer.id,
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
@pytest.mark.parametrize("invalid_manufacturer_id", [-1, 0, 9999])
def test_create_car_with_invalid_country_id(auth_client, invalid_manufacturer_id):
    response = auth_client.post(
        reverse("create_car"),
        data={
            "name": "Passat",
            "end_year": 2023,
            "start_year": 2020,
            "country": invalid_manufacturer_id,
        },
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_car_no_auth(client, country, manufacturer):
    response = client.post(
        reverse("create_car"),
        data={
            "name": "Passat",
            "end_year": 2023,
            "start_year": 2020,
            "manufacturer": manufacturer.id,
        },
    )

    assert response.status_code == 401
