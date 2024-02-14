import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_comment(client, car):
    response = client.post(
        reverse("create_comment"),
        data={"author_email": "test@gmail.com", "car": car.id, "comment": "test"},
    )
    expected_response = {
        "id": response.data.get("id"),
        "author_email": response.data.get("author_email"),
        "car": car.id,
        "comment": response.data.get("comment"),
        "created_at": response.data.get("created_at"),
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
@pytest.mark.parametrize("invalid_car_id", [-1, 0, 9999])
def test_create_comment_with_invalid_car_id(auth_client, invalid_car_id):
    response = auth_client.post(
        reverse("create_car"),
        data={
            "author_email": "test@gmail.com",
            "car": invalid_car_id,
            "comment": "test",
        },
    )

    assert response.status_code == 400
