from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from core.social_auth.views import FacebookSocialAuthView
from core.social_auth.views import GoogleSocialAuthView
from core.views import GetMe
from core.views import UserRegistrationView


urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="signup"),
    path("me/", GetMe.as_view(), name="me"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("google/", GoogleSocialAuthView.as_view()),
    path("facebook/", FacebookSocialAuthView.as_view()),
]
