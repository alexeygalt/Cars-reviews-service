import pytest
from django.urls import reverse
from reviews.serializers import CommentListSerializer


@pytest.mark.django_db
def test_retrieve_comment(client, comment):
    response = client.get(reverse("retrieve_update_delete_comment", args=[comment.pk]))

    expected_response = CommentListSerializer(instance=comment).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve_comment_not_found(client, comment):
    response = client.get(reverse("retrieve_update_delete_comment", args=[12]))
    assert response.status_code == 404
