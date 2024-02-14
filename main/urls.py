from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from main import settings
from django.shortcuts import redirect

urlpatterns = [
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("auth/", include("core.urls")),
    path("", include("reviews.urls")),
]

if settings.URL_PREFIX:
    urlpatterns = [
        path(f"{settings.URL_PREFIX}/", include(urlpatterns)),
        path("admin/", admin.site.urls),
        path("", lambda req: redirect("/api/docs/")),
    ]
