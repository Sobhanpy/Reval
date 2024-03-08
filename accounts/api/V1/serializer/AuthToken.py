from rest_framework import serializers
from django.contrib.auth import authenticate

class CustomeAuthTokenSerializer(serializers.Serializer):
    '''
    This  serializer is used to handle custom auth tokens
    '''
    phone = serializers.CharField(label=("Phone Number"), write_only=True)
    password = serializers.CharField(
        label=("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=("Token"), read_only=True)

    def validate(self, attrs):
        '''
        here we validate user passwords
        '''
        phone = attrs.get("phone")
        password = attrs.get("password")

        if phone and password:
            user = authenticate(
                request=self.context.get("request"), phone=phone, password=password
            )

            if not user:
                message = "Unable to log in with provided credentials."
                raise serializers.ValidationError(message, code="authorization")
            if not user.is_verified:
                massage = "your account is not verified !"
                raise serializers.ValidationError(massage, code="authorization")

        else:
            message = 'Must include "phone" and "password".'
            raise serializers.ValidationError(message, code="authorization")
        attrs["user"] = user
        return attrs