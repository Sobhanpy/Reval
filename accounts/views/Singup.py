from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from accounts.forms import CustomUserForm


class SignUpView(CreateView):
    """
    This class worte for SingUp Users
    """

    template_name = "accounts/signup.html"
    form_class = CustomUserForm
    success_url = "/accounts/login/"

    def form_valid(self, form):
        form.save()
        phone = self.request.POST.get("phone")
        password = self.request.POST.get("password1")
        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(self.request, user)
            return redirect("/")

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "Invalid phone number or password"
        )
        return super().form_invalid(form)
