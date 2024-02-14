import pytest
from django.urls import reverse
from reviews.serializers import CarRetrieveSerializer


@pytest.mark.django_db
def test_retrieve_carr(client, car):
    response = client.get(reverse("retrieve_update_destroy_car", args=[car.pk]))

    expected_response = CarRetrieveSerializer(instance=car).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve_car_not_found(client, car):
    response = client.get(reverse("retrieve_update_destroy_car", args=[4]))
    assert response.status_code == 404
