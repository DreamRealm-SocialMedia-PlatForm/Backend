from .serializers                         import RegisterSerializer
from rest_framework                       import generics
from rest_framework.permissions           import AllowAny
from rest_framework_simplejwt.views       import TokenObtainPairView
from .serializers                         import MyTokenObtainPairSerializer
from django.contrib.auth                  import get_user_model
from rest_framework.views                 import APIView 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response              import Response
from django.contrib.auth                  import login, logout
# 
User = get_user_model()

# General Views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# JWT Views
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

# Session views
class SessionAuthView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({'detail': 'Session login successful.'})

    def delete(self, request):

        logout(request)
        return Response({'detail': 'Session logout successful.'})
