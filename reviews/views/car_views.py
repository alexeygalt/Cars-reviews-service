from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from reviews.models import Car
from rest_framework.permissions import IsAuthenticated
from reviews import serializers


@extend_schema(
    summary="Создание нового Автомобиля",
)
class CreateCarView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarBaseSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    summary="Получение всех Автомобилей",
)
class ListCarsView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarRetrieveSerializer


@extend_schema_view(
    put=extend_schema(summary="Обновление атрибутов ресурса Автомобиль"),
    get=extend_schema(summary="Получение  ресурса Автомобиль"),
    delete=extend_schema(summary="Удаление ресурса Автомобиль"),
)
class RetrieveUpdateDestroyCarView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    http_method_names = [
        "get",
        "put",
        "delete",
    ]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return serializers.CarBaseSerializer
        return serializers.CarRetrieveSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAuthenticated()]
        return super().get_permissions()
