import json 

from django.validation import ValidationError
from django.views import View 
from django.http import JsonResponse

from users.models import User
from users.validation import Validate_email , Validate_password , Validate_emailduplicate

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)

        try:
            name =  




        
        
        
        
        
        
        
        
        
        
        
        user = User.objects.create(name=data["user"])

        return JsonResponse({"message": "SUCCESS"}, status = 201)

        


