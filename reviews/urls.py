from django.urls import path
from django.views.decorators.cache import cache_page

from reviews import views

urlpatterns = [
    path("country/create/", views.CreateCountryView.as_view(), name="create_country"),
    path(
        "country/",
        cache_page(180)(views.ListCountryView.as_view()),
        name="list_all_countrys",
    ),
    path(
        "country/<int:pk>/",
        views.RetrieveUpdateDestroyCountryView.as_view(),
        name="retrieve_update_destroy_county",
    ),
    path(
        "manufacturer/create/",
        views.CreateManufacturerView.as_view(),
        name="create_manufacturer",
    ),
    path(
        "manufacturer/",
        cache_page(180)(views.ListManufacturerView.as_view()),
        name="list_manufacturer",
    ),
    path(
        "manufacturer/<int:pk>/",
        views.RetrieveUpdateDestroyManufacturerView.as_view(),
        name="retrieve_update_destroy_manufacturer",
    ),
    path("car/create/", views.CreateCarView.as_view(), name="create_car"),
    path("car/", cache_page(180)(views.ListCarsView.as_view()), name="list_all_cars"),
    path(
        "car/<int:pk>/",
        views.RetrieveUpdateDestroyCarView.as_view(),
        name="retrieve_update_destroy_car",
    ),
    path("comment/create/", views.CreateCommentView.as_view(), name="create_comment"),
    path(
        "comment/",
        cache_page(180)(views.ListCommentView.as_view()),
        name="list_all_comments",
    ),
    path(
        "comment/<int:pk>/",
        views.RetrieveUpdateDestroyCommentView.as_view(),
        name="retrieve_update_delete_comment",
    ),
    path("export/<str:model_name>/", views.ExportCSVView.as_view(), name="export_csv"),
]
