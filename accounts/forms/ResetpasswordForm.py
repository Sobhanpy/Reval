from django import forms


class ResetpasswordForm(forms.Form):
    """
    this form is used to reset the password of the user
    """

    phone = forms.CharField(
        label=("Phone number"),
        max_length=12,
    )
