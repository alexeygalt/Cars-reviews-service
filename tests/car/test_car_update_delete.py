import pytest
import json
from django.urls import reverse


@pytest.mark.django_db
def test_update_car(auth_client, car, manufacturer):
    response = auth_client.put(
        reverse("retrieve_update_destroy_car", args=[car.pk]),
        data=json.dumps(
            {
                "name": "put test name",
                "start_year": 2001,
                "end_year": 2010,
                "manufacturer": manufacturer.id,
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.data.get("name") == "put test name"
    assert response.data.get("manufacturer") == manufacturer.id


@pytest.mark.django_db
def test_update_car_no_auth(client, manufacturer):
    response = client.put(
        reverse("retrieve_update_destroy_car", args=[manufacturer.pk]),
        data=json.dumps({"name": "put test name", "country": []}),
        content_type="application/json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_car(auth_client, car):
    response = auth_client.delete(reverse("retrieve_update_destroy_car", args=[car.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
def test_update_car_bad_date(auth_client, car, manufacturer):
    response = auth_client.put(
        reverse("retrieve_update_destroy_car", args=[car.pk]),
        data=json.dumps(
            {
                "name": "put test name",
                "start_year": 2010,
                "end_year": 2001,
                "manufacturer": manufacturer.id,
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 400
