#imports
from rest_framework import generics

#models
from django.contrib.auth import get_user_model

#serializers
from .serializers import RegisterSerializer

USER = get_user_model()


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = USER.objects.all()
    serializer_class = RegisterSerializer