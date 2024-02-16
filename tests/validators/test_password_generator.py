import string

import pytest
from rest_framework.exceptions import ValidationError

from core.social_auth.utils import password_generator
from reviews.validators import validate_year_range


@pytest.mark.parametrize(
    "size, chars",
    [
        (None, string.ascii_uppercase + string.ascii_lowercase + string.digits),
        (8, string.ascii_uppercase),
        (12, string.ascii_lowercase),
        (15, string.digits),
        (10, "!@#$%^"),
    ],
)
def test_password_generator(size, chars):
    if size is not None:
        password = password_generator(size=size, chars=chars)
        assert len(password) == size
        assert all(char in chars for char in password)
    else:
        with pytest.raises(TypeError):
            password_generator(size=size, chars=chars)


@pytest.mark.parametrize(
    "start_year, end_year",
    [
        (2000, 2020),
        (2020, 2000),
    ],
)
def test_validate_year_range(start_year, end_year):
    data = {"start_year": start_year, "end_year": end_year}
    if start_year <= end_year:
        assert validate_year_range(data) is None
    else:
        with pytest.raises(ValidationError):
            validate_year_range(data)
