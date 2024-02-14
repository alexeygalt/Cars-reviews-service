from rest_framework import serializers
from reviews.models import Comment, Car


class CarToCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["id", "name", "start_year", "end_year"]


class CommentBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentListSerializer(CommentBaseSerializer):
    car = CarToCommentSerializer()

    class Meta:
        model = Comment
        fields = ["id", "author_email", "created_at", "comment", "car"]
