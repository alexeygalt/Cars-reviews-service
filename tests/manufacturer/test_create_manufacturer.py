import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_manufacturer(auth_client, country):
    response = auth_client.post(
        reverse("create_manufacturer"),
        data={"name": "Russia", "country": country.id},
    )
    expected_response = {
        "id": response.data.get("id"),
        "name": response.data.get("name"),
        "country": response.data.get("country"),
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
@pytest.mark.parametrize("invalid_country_id", [-1, 0, 9999])
def test_create_manufacturer_with_invalid_country_id(auth_client, invalid_country_id):
    response = auth_client.post(
        reverse("create_manufacturer"),
        data={"name": "Toyota", "country": invalid_country_id},
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_create_manufacturer_no_auth(client, country):
    response = client.post(
        reverse("create_manufacturer"),
        data={"name": "Russia", "country": country.id},
    )

    assert response.status_code == 401
