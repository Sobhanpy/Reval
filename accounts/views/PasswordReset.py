from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomeUser
from accounts.forms import ResetpasswordForm
from accounts.SendSMSToken import SendSMSTokenView


class PasswordResetView(FormView):
    """
    This class is for getting user's phone number for reset password
    """

    form_class = ResetpasswordForm
    success_url = "/accounts/resetPassword/done/"
    template_name = "accounts/resetpassword_form.html"

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def form_valid(self, form):
        phone = self.request.POST.get("phone")
        user = get_object_or_404(CustomeUser, phone=phone)
        token = self.get_tokens_for_user(user)
        message = f"""کاربر عزیز با لینک زیر وارد وب  سایت شوید
        http://127.0.0.1:accounts/reset-password/{token}
        """
        to = [phone]
        SendSMSTokenView(target=to, message=message)
        return super().form_valid(form)
