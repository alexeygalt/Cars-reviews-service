from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from reviews import serializers
from reviews.models import Manufacturer


@extend_schema(
    summary="Создание нового производителя",
)
class CreateManufacturerView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerBaseSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    summary="Получение всех производителей",
)
class ListManufacturerView(ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerRetrieveSerializer


@extend_schema_view(
    put=extend_schema(summary="Обновление атрибутов ресурса Производитель"),
    get=extend_schema(summary="Получение  ресурса Производитель"),
    delete=extend_schema(summary="Удаление ресурса Производитель"),
)
class RetrieveUpdateDestroyManufacturerView(RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    http_method_names = [
        "get",
        "put",
        "delete",
    ]

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return serializers.ManufacturerBaseSerializer
        return serializers.ManufacturerRetrieveSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAuthenticated()]
        return super().get_permissions()
