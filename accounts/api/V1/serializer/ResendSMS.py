from rest_framework import serializers
from django.shortcuts import get_object_or_404
from accounts.models import CustomeUser

class ResendSMSSerializer(serializers.Serializer):
    '''
    this class resend phone for user
    '''
    phone = serializers.CharField(label=("Phone Number"), write_only=True)

    def validate(self, attrs):
        '''this function check user phone'''
        user = get_object_or_404(CustomeUser, phone=attrs.get("phone"))
        attrs["user"] = user
        return attrs