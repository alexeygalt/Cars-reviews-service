from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from reviews.models import Comment
from rest_framework.permissions import IsAuthenticated
from reviews import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


@extend_schema(
    summary="Создание нового комментария",
)
class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentBaseSerializer


@extend_schema(
    summary="Получение всех комментариев",
)
class ListCommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    ordering_fields = ("created_at",)


@extend_schema_view(
    put=extend_schema(summary="Обновление атрибутов ресурса Комментарий"),
    delete=extend_schema(summary="Удаление ресурса Комментарий"),
    get=extend_schema(summary="Получение  ресурса Комментарий"),
)
class RetrieveUpdateDestroyCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    http_method_names = [
        "get",
        "put",
        "delete",
    ]

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return serializers.CommentListSerializer
        return serializers.CommentBaseSerializer
