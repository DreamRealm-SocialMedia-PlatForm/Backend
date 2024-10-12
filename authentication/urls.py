
from django.urls import path
from .views import MyObtainTokenPairView, RegisterView, SessionAuthView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    # General
    path('register/'       , RegisterView.as_view()         , name='auth_register'),
    # JWT
    # bearer {token}
    path('login/'          , MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/'  , TokenRefreshView.as_view()     , name='token_refresh'),

    # AuthToken
    # Token {token}
    path("api/login/"      , obtain_auth_token              , name="login_with_token"),

    # SessionAuth
    # Post for login 
    # Delete for logout
    path("web/"            , SessionAuthView                , name="auth_with_session")


]
