from django.views.generic import TemplateView


class ChangePasswordDoneView(TemplateView):
    """
    When reset password process is completely done
    """

    template_name = "accounts/changepassword_complete.html"
