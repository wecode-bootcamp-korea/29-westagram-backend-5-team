import json

from django.core.exceptions import ValidationError
from django.http            import JsonResponse
from django.views           import View

import bcrypt

from users.models     import User
from users.validators import validate_email, validate_password, validate_email_duplicate

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
            user     = User.objects.get(email=email)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER (email)"}, status=401)

        if password != user.password:
            return JsonResponse({"message": "INVALID_USER (password)"}, status=401)

        return JsonResponse({"message": "SUCCESS"}, status=200)