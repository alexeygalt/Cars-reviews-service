import csv
import openpyxl
from django.http import HttpResponse
from rest_framework.views import APIView
from django.apps import apps
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django.db import models
from rest_framework.exceptions import ValidationError


@extend_schema(
    summary="Экспорт",
    description="Экспорт данных в CSV или XLSX формат",
    parameters=[
        OpenApiParameter(
            name="model_name",
            required=True,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.PATH,
            description="Название модели :(Country, Manufacturer, Car, Comment)",
        ),
        OpenApiParameter(
            name="key",
            required=False,
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            enum=["csv", "xlsx"],
        ),
    ],
    responses={200: "CSV or XLSX file"},
)
class ExportCSVView(APIView):
    def get(self, request, model_name):
        key_format = request.query_params.get("key", "csv")
        if key_format == "csv":
            return self.export_csv(model_name)
        elif key_format == "xlsx":
            return self.export_xlsx(model_name)
        return HttpResponse("Invalid format", status=400)

    def export_csv(self, model_name):
        response = HttpResponse(content_type="text/csv")
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{model_name}_export.csv"'

        writer = csv.writer(response)

        try:
            model = apps.get_model(app_label="reviews", model_name=model_name)
        except LookupError:
            raise ValidationError("Model not found")

        writer.writerow([field.verbose_name for field in model._meta.fields])

        for obj in model.objects.all():
            writer.writerow([getattr(obj, field.name) for field in model._meta.fields])

        return response

    def export_xlsx(self, model_name):
        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{model_name}_export.xlsx"'
        wb = openpyxl.Workbook()
        ws = wb.active

        try:
            model = apps.get_model(app_label="reviews", model_name=model_name)
        except LookupError:
            raise ValidationError("Model not found")

        fields = [field.verbose_name for field in model._meta.fields]
        ws.append(fields)
        for obj in model.objects.all():
            row_data = []
            for field in model._meta.fields:
                if isinstance(field, models.ForeignKey):
                    related_obj = getattr(obj, field.name)
                    if related_obj:
                        row_data.append(str(related_obj))
                    else:
                        row_data.append("")
                else:
                    row_data.append(getattr(obj, field.name))
            ws.append(row_data)

        wb.save(response)

        return response
