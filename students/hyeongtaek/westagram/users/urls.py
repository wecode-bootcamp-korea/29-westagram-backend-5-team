from django.urls import path, include


from users.views import SignupView

urlpatterns = [

    path('', SignUpView.as_view()),

]