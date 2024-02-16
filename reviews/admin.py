from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from reviews.models import Car
from reviews.models import Comment
from reviews.models import Country
from reviews.models import Manufacturer


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author_email", "car_link", "created_at")
    search_fields = ("id", "author_email__startswith")
    ordering = (
        "id",
        "created_at",
        "author_email",
    )
    list_filter = ("car",)

    def car_link(self, comment):
        url = reverse("admin:reviews_car_change", args=[comment.car.id])
        link = f'<a href="{url}">{comment.car.__str__()}</a>'
        return mark_safe(link)

    car_link.short_description = "Авто"


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "manufacturer_link", "start_year", "end_year")
    search_fields = ("id", "name__startswith")
    ordering = (
        "id",
        "start_year",
        "end_year",
        "manufacturer",
    )
    list_filter = ("manufacturer",)

    def manufacturer_link(self, car: Car):
        url = reverse("admin:reviews_manufacturer_change", args=[car.manufacturer.id])
        link = f'<a href="{url}">{car.manufacturer.__str__()}</a>'
        return mark_safe(link)

    manufacturer_link.short_description = "Производитель"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    search_fields = ("id", "name__startswith")
    ordering = (
        "id",
        "name",
    )


@admin.register(Manufacturer)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country_link")
    search_fields = ("id", "name__startswith")
    ordering = (
        "id",
        "name",
    )

    def country_link(self, manufacturer: Manufacturer):
        url = reverse("admin:reviews_country_change", args=[manufacturer.country.id])
        link = f'<a href="{url}">{manufacturer.country.__str__()}</a>'
        return mark_safe(link)

    country_link.short_description = "Страна"
