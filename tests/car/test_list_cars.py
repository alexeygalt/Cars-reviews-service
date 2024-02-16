import pytest
from django.urls import reverse

from reviews.serializers import CarRetrieveSerializer
from tests import factories


@pytest.mark.django_db
def test_list_car(
    client,
):
    cars = factories.CarFactory.create_batch(5)

    response = client.get(reverse("list_all_cars"))

    expected_response = CarRetrieveSerializer(instance=cars, many=True).data

    assert response.status_code == 200
    assert response.data == expected_response
