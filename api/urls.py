
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('messages/',views.MessagesAPI.as_view()),
    path('register/',views.RegisterUserAPIView.as_view()),
    path('login/', obtain_auth_token)


    
]
