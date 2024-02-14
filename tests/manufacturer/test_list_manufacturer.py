import pytest
from django.urls import reverse
from reviews.serializers import ManufacturerRetrieveSerializer
from tests import factories


@pytest.mark.django_db
def test_list_manufacturer(client, new_user):
    manufacturers = factories.ManufacturerFactory.create_batch(5)

    response = client.get(reverse("list_manufacturer"))

    expected_response = ManufacturerRetrieveSerializer(
        instance=manufacturers, many=True
    ).data

    assert response.status_code == 200
    assert response.data == expected_response
