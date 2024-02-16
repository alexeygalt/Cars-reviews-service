import pytest
from django.urls import reverse

from reviews.serializers import CountryRetrieveSerializer
from tests import factories


@pytest.mark.django_db
def test_list_countries(client, new_user):
    countries = factories.CountryFactory.create_batch(5)

    response = client.get(reverse("list_all_countrys"))

    expected_response = CountryRetrieveSerializer(instance=countries, many=True).data

    assert response.status_code == 200
    assert response.data == expected_response
