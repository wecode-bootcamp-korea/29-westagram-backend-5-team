import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validators import validate_email, validate_password, validate_duplicate


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)

        name     = data['name']
        email    = data['email']
        password = data['password']
        phone    = data['phone']

        if not validate_email(email):
            return JsonResponse({"message":"KEY_ERROR (email)"}, status=400)

        if not validate_password(password):
            return JsonResponse({"message":"KEY_ERROR (password)"}, status=400)

        if validate_duplicate(email):
            return JsonResponse({"message":"KEY_ERROR (email duplicate)"}, status=400)

        User.objects.create(
            name     = name,
            email    = email,
            password = password,
            phone    = phone,
        )

        return JsonResponse({"message":"SUCCESS"}, status=201)

