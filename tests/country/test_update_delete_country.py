import pytest
import json
from django.urls import reverse


@pytest.mark.django_db
def test_update_country(auth_client, country):
    response = auth_client.put(
        reverse("retrieve_update_destroy_county", args=[country.pk]),
        data=json.dumps({"name": "put test name", "manufacturers": []}),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.data.get("name") == "put test name"


@pytest.mark.django_db
def test_update_country_no_auth(client, country):
    response = client.put(
        reverse("retrieve_update_destroy_county", args=[country.pk]),
        data=json.dumps({"name": "put test name", "manufacturers": []}),
        content_type="application/json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_country(auth_client, country):
    response = auth_client.delete(
        reverse("retrieve_update_destroy_county", args=[country.pk])
    )

    assert response.status_code == 204
