from rest_framework import serializers
from reviews.models import Country, Manufacturer


class ManufacturerToCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name"]


class CountryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CountryRetrieveSerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerToCountrySerializer(
        many=True, read_only=True, source="manufacturer_set"
    )

    class Meta:
        model = Country
        fields = ["id", "name", "manufacturers"]
