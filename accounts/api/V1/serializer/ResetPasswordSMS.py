from rest_framework import serializers
from django.shortcuts import get_object_or_404
from accounts.models import CustomeUser

class ResetPasswordSMSSerializer(serializers.Serializer):
    '''
    We write this class for reset pass word with phone
    first we check the phone and if is existed send phone
    '''
    phone = serializers.CharField(label=("Phone Number"), write_only=True)

    def validate(self, attrs):
        '''
        this function check user phone
        '''
        user = get_object_or_404(CustomeUser, phone=attrs.get("phone"))
        attrs["user"] = user
        return attrs
