from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import UserRegister, UserLogin, Home

urlpatterns = [
    url(r'^/login/', UserLogin, name='login'),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^/register/', UserRegister.as_view()),
    url(r'^/home/', Home.as_view()),
]
