from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError


class PasswordChangeForm(SetPasswordForm):
    """
    this form is used to change the password of the user
    and to check if the old password entered is correct
    """

    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": ("Your old Password is not True. Please enter it again."),
    }
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        this function checks if the old password entered is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password
