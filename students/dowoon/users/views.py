import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password, validate_duplicate


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            name     = data['name']
            email    = data['email']
            password = data['password']
            phone    = data['phone']

            if email == "" or password == "":
                raise Exception("ERROR : email or password is blank")

            validate_email(email)
            validate_password(password)
            validate_duplicate(email)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
        except Exception as e:
            return JsonResponse({"message" : str(e)}, status=400)

        User.objects.create(
            name     = name,
            email    = email,
            password = password,
            phone    = phone,
        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)

