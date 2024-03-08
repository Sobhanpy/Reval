from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.api.V1.serializer import ResetPasswordSMSSerializer
from accounts.SendSMSToken import SendSMSTokenView


class ResetPasswordSMSView(GenericAPIView):
    serializer_class = ResetPasswordSMSSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user)
        message = f'''
                            کاربر عزیز با لینک زیر به سایت برگردید
            http://127.0.0.1:8000/accounts/api/V1/reset-password/{token}
        '''
        to=[serializer.validated_data["phone"]]
        SendSMSTokenView(target=to, message=message)
        return Response({"detail": "sms Resend for you..."})

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
