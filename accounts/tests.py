from django.test import TestCase, Client
from accounts.models import (
    CustomeUser,
    CustomeBaseUserManager,
)
from accounts.forms import (
    AuthenticationForm,
    CustomUserForm,
    PasswordChangeForm,
    ResetpasswordDone,
    ResetpasswordForm,
)
from accounts.views import (
    LoginView,
    LogoutView,
    SignUpView,
    ChangePasswordDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    ResetDoneView,
    PasswordChangeView,
)

class TestAccount(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomeUser.objects.create_user(
            email="sobhan@test.com",
            password="Hala123boro..",
        )
        