import json
import re

from django.http import JsonResponse
from django.core.exceptions import ValidationError 
from django.views import View 

from users.models import User

REGEX_EMAIL = "^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
REGEX_PASSWORD = "^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$"
 
class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            name          = data['name']
            email         = data['email']
            password      = data['password']
            phone_number  = data['phone_number']

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'EMAIL_ALREADY_EXISTS'}, status=400)    
            
            if not re.match(REGEX_EMAIL , email):
                return JsonResponse({"message" : "INVALID_EMAIL"}, status = 400)

            if not re.match(REGEX_PASSWORD , password):
                return JsonResponse({"message" : "INVALID_PASSWORD"}, status = 400)

            User.objects.create(
                name          = name,
                email         = email,
                password      = password,
                phone_number  = phone_number,
            )

            return JsonResponse({"message" : "SUCCESS"}, status = 201) 
    
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=401)


class LogInView(View):
    def post(self,request):
        data = json.loads(request.body) 
        try: 
            if not User.objects.filter(
                email    = data['email'],
                password = data['password'],
                ).exists():
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            return JsonResponse({'message':'SUCCESS'},status=200) 

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)