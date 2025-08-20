#imports
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

#models
from django.contrib.auth import get_user_model
from account.models import Profile

#consts
USER = get_user_model()

#serializers
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type':'password'}
    )
    
    class Meta:
        model = USER
        fields = (
            'name',
            'username',
            'email',
            'password',
            'confirm_password',
            'image',
        )
        
        extra_kwargs = {'password' : {'write_only': True}}
        
    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(_("Passwords do not match."))
        
        data.pop('confirm_password')
        
        return data
        
    def save(self, **kwargs):
        fields = self.validated_data
        password = fields.pop('password')
        user = USER.objects.create(**fields)
        user.set_password(password)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        style={'input_type': 'text'}
    )
    
    password = serializers.CharField(
        required=True,
        style={'input_text' : 'password'},
        write_only=True
    )
        
    def validate(self, data):
        user = USER.objects.filter(username=data.get('username')).first()
        
        if not user:
            raise serializers.ValidationError(_("User not found."))
        
        if not user.check_password(data.get('password')):
            raise serializers.ValidationError(_("Incorrect password."))
        
        return data
    
    def save(self, **kwargs):
        user = USER.objects.get(username=self.data.get('username'))
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ('username','name','image')
    
class ProfileSerializer(serializers.ModelSerializer):
    user =  UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = ('user','bio','banner')