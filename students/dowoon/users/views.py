import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View

from users.models import User
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
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except ValidationError as e:
            return JsonResponse({"message" : str(e)}, status=400)

        User.objects.create(
            name     = name,
            email    = email,
            password = password,
            phone    = phone,
        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)

