from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from reviews import serializers
from reviews.models import Country


@extend_schema(
    summary="Создание новой страны",
)
class CreateCountryView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = serializers.CountryBaseSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    summary="Получение всех стран",
)
class ListCountryView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = serializers.CountryRetrieveSerializer


@extend_schema_view(
    put=extend_schema(summary="Обновление атрибутов ресурса Страна"),
    get=extend_schema(summary="Получение  ресурса Страна"),
    delete=extend_schema(summary="Удаление ресурса Страна"),
)
class RetrieveUpdateDestroyCountryView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = serializers.CountryRetrieveSerializer
    http_method_names = [
        "get",
        "put",
        "delete",
    ]

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAuthenticated()]
        return super().get_permissions()
