#imports
from rest_framework import generics
from api.core.mixins import SuccessfulMessageMixin
from api.account.utills import SetAcessToken
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response


#models
from django.contrib.auth import get_user_model

#serializers
from .serializers import RegisterSerializer,LoginSerializer

USER = get_user_model()


# Create your views here.
class RegisterView(
    SuccessfulMessageMixin,
    SetAcessToken,
    generics.CreateAPIView,
):
    message = _('Created successfully')
    queryset = USER.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        self.set_token(response,user)
        self.set_message(response)
        return response
        
    
    
class LoginView(
    SuccessfulMessageMixin,
    SetAcessToken,
    generics.CreateAPIView,
):
    message = _('Login successful')
    queryset = USER.objects.all()
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        self.set_token(response,user)
        self.set_message(response)
        return response
    
