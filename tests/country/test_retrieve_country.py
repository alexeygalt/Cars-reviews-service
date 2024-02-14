import pytest
from django.urls import reverse
from reviews.serializers import CountryRetrieveSerializer


@pytest.mark.django_db
def test_retrieve_country(client, country):
    response = client.get(reverse("retrieve_update_destroy_county", args=[country.pk]))

    expected_response = CountryRetrieveSerializer(instance=country).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve_country_not_found(client, country, manufacturer):
    response = client.get(reverse("retrieve_update_destroy_county", args=[4]))
    assert response.status_code == 404
