#imports
from rest_framework.response import Response
from rest_framework import status

#mixin

class SuccessfulMessageMixin:
    message = None
    
    def get_message(self):
        if not self.message:
            raise NotImplementedError("You must define a 'message' attribute.")
        
        return self.message
    
    def set_message(self,response):
        try:
            message = self.get_message()
            response.data['message'] = message
            return response
        
        except NotImplementedError as e: 
            raise e
    
    def post(self,request,*args, **kwargs):
           response = super().post(request, *args, **kwargs)
           return self.set_message(response)