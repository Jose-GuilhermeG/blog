#imports
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

#consts
USER = get_user_model()


#mixins
class CreateUserToken:
    @staticmethod
    def create_user_token(user):
        if not user:
            raise NotImplementedError("User must be provided to create a token.")
        
        if not user.is_active:
            raise ValueError("Cannot create token for inactive user.")
        
        refresh = RefreshToken.for_user(user)
        
        return refresh.access_token, refresh
    
    
class SetAcessToken(
    CreateUserToken,
):
    def set_token(self, response,user, *args, **kwargs):
        
        access_token, refresh_token = self.create_user_token(user)
        
        response.data['access'] = str(access_token)
        response.data['refresh'] = str(refresh_token)
        
        response.set_cookie(
            key = 'access',
            value = str(access_token)
        )
        response.set_cookie(
            key = 'refresh',
            value = str(refresh_token)
        )
        
        return response