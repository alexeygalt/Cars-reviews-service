from rest_framework import serializers
from reviews.models import Car, Manufacturer, Comment
from reviews.validators import validate_year_range


class CommentToCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author_email", "created_at", "comment"]


class ManufacturerToCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name"]


class CarBaseSerializer(serializers.ModelSerializer):
    def validate(self, data):
        validate_year_range(data)
        return data

    class Meta:
        model = Car
        fields = "__all__"


class CarRetrieveSerializer(CarBaseSerializer):
    manufacturer = ManufacturerToCarSerializer()
    comments = CommentToCarSerializer(many=True, read_only=True, source="comment_set")
    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "name",
            "start_year",
            "end_year",
            "comments_count",
            "comments",
            "manufacturer",
        ]

    def get_comments_count(self, obj: Car):
        return Comment.objects.filter(
            car=obj,
        ).count()
