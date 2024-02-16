import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import User
from tests import factories


@pytest.fixture
def new_user(db):
    user = User.objects.create_user(username="testname", email="test@mail.ru", password="testSuper1Password")
    return user


@pytest.fixture
def auth_client(new_user):
    client = APIClient()
    token = RefreshToken.for_user(new_user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token.access_token}")
    return client


@pytest.fixture
def country():
    return factories.CountryFactory.create()


@pytest.fixture
def manufacturer(country):
    return factories.ManufacturerFactory.create(country=country)


@pytest.fixture
def car(manufacturer):
    return factories.CarFactory.create(manufacturer=manufacturer)


@pytest.fixture
def comment(car):
    return factories.CommentFactory.create(car=car)
