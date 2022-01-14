import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password, validate_duplicate


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        name     = data['name']
        email    = data['email']
        password = data['password']
        phone    = data['phone']

        try:
            validate_email(email)
            validate_password(password)
            validate_duplicate(email)
        except ValidationError:
            return JsonResponse({"message" : "KEY_ERROR (ValidationError)"}, status=400)
        except User.DoesNotExist:
            pass

        User.objects.create(
            name     = name,
            email    = email,
            password = password,
            phone    = phone,
        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)

