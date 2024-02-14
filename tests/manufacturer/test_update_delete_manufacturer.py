import pytest
import json
from django.urls import reverse


@pytest.mark.django_db
def test_update_manufacturer(auth_client, manufacturer, country):
    response = auth_client.put(
        reverse("retrieve_update_destroy_manufacturer", args=[manufacturer.pk]),
        data=json.dumps({"name": "put test name", "country": country.id}),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.data.get("name") == "put test name"
    assert response.data.get("country") == country.id


@pytest.mark.django_db
def test_update_manufacturer_no_auth(client, manufacturer):
    response = client.put(
        reverse("retrieve_update_destroy_manufacturer", args=[manufacturer.pk]),
        data=json.dumps({"name": "put test name", "country": []}),
        content_type="application/json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_manufacturer(auth_client, manufacturer):
    response = auth_client.delete(
        reverse("retrieve_update_destroy_manufacturer", args=[manufacturer.pk])
    )

    assert response.status_code == 204
