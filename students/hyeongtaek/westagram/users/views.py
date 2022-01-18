import json
import re


from django.core.exceptions import ValidationError 
from django.views import View 
from django.http import JsonResponse


from users.models import User

regex_email = "^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
regex_password = "^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$"
 

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
    
        
       
        if not re.match("^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"):
            raise User.email({"ERROR": "맞지 않는 메일주소입니다"}, status=400)
              
    
        if not re.match("^(?=.{8,16}$)(?=.*[a-z])(?=.*[0-9]).*$"):
            raise User.password({"ERROR": "Invalid Password"}, status=400)
        
        elif len(regex_password)<8:
            raise User.password({"ERROR": "비밀번호는 8자이상입력"}, status=400)


class LoginView(View):
    def post(self,request):
        data = json.loads(request.body) 
        try: 
            if data['email'] and data['password'] == '':
                return JsonResponse({"message':'Email or Password is Blank"}, status = 400)

            if data['email'] != regex_email:
                return JsonResponse({'message': 'Invalid Email'},status=401)


            if data['password'] != regex_password:
                return JsonResponse({'message': 'Invalid Email'},status=401)

        except ValueError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=401)

        else:
            User.objects.create(
                name        = data['name'],
                email       = data['email'],
                password    = data['password'],
                phonenumber     = data['phonenumber'],
            )
            return JsonResponse({'message':'SUCCESS'},status=201) 