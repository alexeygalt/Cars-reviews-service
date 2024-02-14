from rest_framework import serializers
from .car_serializers import CarBaseSerializer, CarRetrieveSerializer
from .comment_serializer import CommentBaseSerializer, CommentListSerializer
from .country_serializers import CountryBaseSerializer, CountryRetrieveSerializer
from .manufacturer_serializers import (
    ManufacturerBaseSerializer,
    ManufacturerRetrieveSerializer,
)


__all__ = (
    "serializers",
    "CarBaseSerializer",
    "CarRetrieveSerializer",
    "CommentBaseSerializer",
    "CommentListSerializer",
    "CountryBaseSerializer",
    "CountryRetrieveSerializer",
    "ManufacturerBaseSerializer",
    "ManufacturerRetrieveSerializer",
)
