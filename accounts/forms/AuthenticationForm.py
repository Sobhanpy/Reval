from django import forms


class AuthenticationForm(forms.Form):
    """
    this form is used to authenticate the user
    """

    phone = forms.CharField(max_length=12, label=("Phone Number"))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password"}
        ),
    )
