from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.api.V1.serializer import CustomObtainPairSerializer


class Customejwtview(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer