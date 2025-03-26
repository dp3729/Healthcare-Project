from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        return Response(
            {
                "user": serializer.data,
                "refresh_token": str(refresh),
                "access_token": str(access_token),
            },
            status=status.HTTP_201_CREATED
        )

# Login User View
class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)

        if user:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            return Response(
                {
                    "message": "Login successful",
                    "refresh_token": str(refresh),
                    "access_token": str(access_token),
                },
                status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Invalid email or password"},
            status=status.HTTP_400_BAD_REQUEST
        )


