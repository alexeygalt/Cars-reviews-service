import pytest
from django.urls import reverse
from reviews.serializers import ManufacturerRetrieveSerializer


@pytest.mark.django_db
def test_retrieve_manufacturer(client, manufacturer):
    response = client.get(
        reverse("retrieve_update_destroy_manufacturer", args=[manufacturer.pk])
    )

    expected_response = ManufacturerRetrieveSerializer(instance=manufacturer).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve_manufacturer_not_found(client, manufacturer):
    response = client.get(reverse("retrieve_update_destroy_manufacturer", args=[4]))
    assert response.status_code == 404
