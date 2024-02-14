import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_country(auth_client):
    response = auth_client.post(
        reverse("create_country"),
        data={
            "name": "Russia",
        },
    )
    expected_response = {
        "id": response.data.get("id"),
        "name": response.data.get("name"),
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_country_no_auth(client):
    response = client.post(
        reverse("create_country"),
        data={
            "name": "Russia",
        },
    )

    assert response.status_code == 401
