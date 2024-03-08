from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomObtainPairSerializer(TokenObtainPairSerializer):
    '''
    This class worte for CustomObtainPairSerializer
    '''
    def validate(self, attrs):
        '''
        here we validate user phone and id
        '''
        validated_data = super().validate(attrs)
        if not self.user.is_verified:
            message = "your account is not verified !"
            raise serializers.ValidationError(message, code="authorization")
        validated_data["id"] = self.user.id
        validated_data["phone"] = self.user.phone
        return validated_data
