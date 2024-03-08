from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from accounts.api.V1.views import (
    RegistrationView,
    CustomeObtainAuthToken,
    DestroyAuthToken,
    ChangePasswordView,
    IsVerifiedView,
    ResendSMSView,
    ResetPasswordSMSView,
    ResetPasswordView,
    Customejwtview,
)

app_name = "api-v1-accounts"

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("token/login/", CustomeObtainAuthToken.as_view(), name="login"),
    path("token/logout/", DestroyAuthToken.as_view(), name="logout"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("is-verified/<str:token>", IsVerifiedView.as_view(), name="is-verification"),
    path("resend/", ResendSMSView.as_view(), name="resend"),
    path(
        "reset-password-sms/",
        ResetPasswordSMSView.as_view(),
        name="reset-password-sms",
    ),
    path(
        "reset-password/<str:token>", ResetPasswordView.as_view(), name="reset-password"
    ),
    # jwt token
    path("token/create/", Customejwtview.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]