from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from accounts.forms import AuthenticationForm


class LoginView(FormView):
    """
    This class wrote for LogIn Users
    """

    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def form_valid(self, form):
        phone = self.request.POST.get("phone")
        password = self.request.POST.get("password")
        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
