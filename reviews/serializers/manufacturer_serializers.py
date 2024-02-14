from rest_framework import serializers
from reviews.models import Manufacturer, Car
from reviews.serializers.car_serializers import CarRetrieveSerializer
from reviews.serializers.country_serializers import CountryBaseSerializer


class CarToManufacturerSerializer(CarRetrieveSerializer):
    class Meta:
        model = Car
        fields = ["id", "name", "start_year", "end_year", "comments_count"]


class ManufacturerBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class ManufacturerRetrieveSerializer(serializers.ModelSerializer):
    country = CountryBaseSerializer()
    cars = CarToManufacturerSerializer(many=True, read_only=True, source="car_set")

    class Meta:
        model = Manufacturer
        fields = ["id", "name", "country", "cars"]
