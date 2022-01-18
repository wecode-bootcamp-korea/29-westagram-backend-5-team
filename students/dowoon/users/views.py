import json

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View

import bcrypt
import jwt

from users.models     import User
from users.validators import validate_email, validate_password, validate_email_duplicate

from my_settings import JWT_SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            name     = data['name']
            email    = data['email']
            password = data['password']
            phone    = data['phone']

            validate_email(email)
            validate_password(password)
            validate_email_duplicate(email)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            hashed_password = hashed_password.decode('utf-8')

            User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password,
                phone    = phone,
            )

            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except ValidationError as e:
            return JsonResponse({"message" : e.message}, status=400)

class LoginView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email = email)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER (email)"}, status=401)

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return JsonResponse({"message": "INVALID_USER (password)"}, status=401)

        access_token = jwt.encode({'id': user.id}, JWT_SECRET_KEY, algorithm = ALGORITHM)

        return JsonResponse({"message": "SUCCESS", "jwt": access_token}, status=200)