import json
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validator import *
from westagram.settings import SECRET_KEY

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
                password    = hashed_password.decode('utf-8'),
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
            user = User.objects.get(email = email)

            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_USER'}, status = 401)

            token = jwt.encode({'users_id': user.id}, SECRET_KEY, algorithm='HS256')

            return JsonResponse({'token' : token}, status=200)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)