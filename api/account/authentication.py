from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication

USER = get_user_model()

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            access = request.COOKIES.get('access')
            if not access:
                return None
            user = USER.objects.get(id=AccessToken(access).get('user_id'))
            return (user,access)
        except:
            return None