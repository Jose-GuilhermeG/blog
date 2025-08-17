#imports
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

#models
from django.contrib.auth import get_user_model

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
        
    def validate(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(_("Passwords do not match."))
        
        return data
        
    def save(self, **kwargs):
        fields = self.data
        password = fields.pop('password')
        user = USER(**fields)
        user.set_password(password)
        user.save()
        return user