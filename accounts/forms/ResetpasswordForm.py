from django import forms


class ResetpasswordForm(forms.Form):
    """
    this form is used to reset the password of the user
    """

    phone = forms.CharFieldField(
        label=("Phone number"),
        max_length=12,
        widjet=forms.TextInput(attrs={"autocomplete": "phone number"}),
    )
