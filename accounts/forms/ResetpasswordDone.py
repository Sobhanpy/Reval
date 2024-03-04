from django import forms


class ResetpasswordDone(forms.Form):
    """
    this form is used to reset the password of the user
    """

    new_password1 = forms.CharField(
        label=("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new_password1"}),
    )

    new_password2 = forms.CharField(
        label=("New password confirm"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new_password2"}),
    )
