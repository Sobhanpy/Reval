from django.views.generic import TemplateView


class ResetDoneView(TemplateView):
    """
    When reset password process is completely done
    """

    template_name = "accounts/resetpassword_complete.html"
