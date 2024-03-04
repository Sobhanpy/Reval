from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomeUser


class CustomUserForm(UserCreationForm):
    """
    this class is used to create a user form
    """

    class Meta:
        model = CustomeUser
        fields = ["phone", "username", "password1", "password2"]
