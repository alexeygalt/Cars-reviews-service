import factory
import random
import string
from core.models import User
from reviews.models import Country, Manufacturer, Car, Comment
from datetime import datetime


def generate_name():
    return "".join(random.choices(string.ascii_letters, k=random.randint(1, 32)))


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")
    password = "superPassword21"


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.LazyFunction(generate_name)


class ManufacturerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manufacturer

    name = factory.LazyFunction(generate_name)
    country = factory.SubFactory(CountryFactory)


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    name = factory.LazyFunction(generate_name)
    manufacturer = factory.SubFactory(ManufacturerFactory)
    start_year = factory.LazyAttribute(lambda x: random.randint(1950, 2023))
    end_year = factory.LazyAttribute(lambda obj: random.randint(obj.start_year, 2023))


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    author_email = factory.Faker("email")
    car = factory.SubFactory(CarFactory)
    comment = factory.Faker("text")
    created_at = factory.LazyAttribute(lambda _: datetime.now())
