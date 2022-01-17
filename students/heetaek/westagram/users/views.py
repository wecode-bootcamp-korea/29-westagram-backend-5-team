import json
import bcrypt

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validator import *

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            name        = data["name"]
            email       = data["email"]
            password    = data["password"]
            phone       = data["phone"]

            is_email(email)
            is_password(password)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            User.objects.create(
                name        = name,
                email       = email,
                password    = hashed_password,
                phone       = phone
            )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

class LoginView(View):
    def post(self,request):
        try:
            data     = json.loads(request.body)
            email    = data["email"]
            password = data["password"]

            user_data = User.objects.filter(email = email, password = password)

            if not user_data:
                return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

            return JsonResponse({'message' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)