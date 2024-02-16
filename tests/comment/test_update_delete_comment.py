import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_update_comment(auth_client, comment, car):
    response = auth_client.put(
        reverse("retrieve_update_delete_comment", args=[comment.pk]),
        data=json.dumps({"author_email": "test@test.com", "car": car.id, "comment": "test"}),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.data.get("author_email") == "test@test.com"
    assert response.data.get("car") == car.id


@pytest.mark.django_db
def test_update_comment_no_auth(client, comment, car):
    response = client.put(
        reverse("retrieve_update_delete_comment", args=[comment.pk]),
        data=json.dumps({"author_email": "test@test.com", "car": car.id, "comment": "test"}),
        content_type="application/json",
    )

    assert response.status_code == 401


@pytest.mark.django_db
def test_delete_comment(auth_client, comment):
    response = auth_client.delete(reverse("retrieve_update_delete_comment", args=[comment.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize(
    "new_author_email, new_car_id, new_comment, expected_status",
    [
        ("", 1, "test", 400),
        ("test", 1, "test", 400),
        ("test@test.com", -1, "test", 400),
        ("test@test.com", 9999, "test", 400),
    ],
)
def test_update_comment_bad_data(
    auth_client,
    comment,
    car,
    new_author_email,
    new_car_id,
    new_comment,
    expected_status,
):
    response = auth_client.put(
        reverse("retrieve_update_delete_comment", args=[comment.pk]),
        data=json.dumps(
            {
                "author_email": new_author_email,
                "car": new_car_id,
                "comment": new_comment,
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == expected_status
