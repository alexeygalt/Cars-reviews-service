import pytest
from django.urls import reverse
from reviews.serializers import CommentListSerializer
from tests import factories


@pytest.mark.django_db
def test_list_comments(client):
    comments = factories.CommentFactory.create_batch(1)

    response = client.get(reverse("list_all_comments"))
    expected_response = CommentListSerializer(instance=comments, many=True).data

    assert response.status_code == 200
    assert response.data == expected_response
