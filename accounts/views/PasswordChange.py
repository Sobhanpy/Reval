from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import PasswordChangeForm


class PasswordChangeView(LoginRequiredMixin, FormView):
    """
    This is class for changing password  process
    """

    template_name = "accounts/changepassword_form.html"
    form_class = PasswordChangeForm
    success_url = "/accounts/change-password/done/"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
