from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.SendSMSToken import SendSMSTokenView
from accounts.api.V1.serializer import RegisterationSerializer
from accounts.models import CustomeUser

class RegistrationView(GenericAPIView):
    '''
    this class is for register users
    '''
    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        '''
        this function validate and create a user
        '''
        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                CustomeUser, phone=serializer.validated_data["phone"]
            )
            token = self.get_tokens_for_user(user)
            message = f'''
                              کاربر عزیز با لینک زیر به سایت برگردید
                http://127.0.0.1:8000/accounts/api/V1/is-verified/{token}
            '''
            to=[serializer.validated_data["phone"]]
            SendSMSTokenView(target=to, message=message)
            return Response({"detail": "phone sent for your verification...!"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)