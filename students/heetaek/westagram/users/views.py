import json

from django.http import JsonResponse
from django.views import View

from users.models import User
from users.validator import *

class SignUp(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            name        = data["name"]
            email       = data["email"]
            password    = data["password"]
            phone       = data["phone"]

            if is_email(email) == False:
                return JsonResponse ({'message':'E-mail is not valid'}, status = 400)

            if is_password(password) == False:
                return JsonResponse({'message':'Password is not valid'}, status = 400)

            User.objects.create(
                name        = name,
                email       = email,
                password    = password,
                phone       = phone
            )
            return JsonResponse({'message':'SUCCESS'},status = 201)
            
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status = 400)

