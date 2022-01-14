from django.urls import path, include

from users.views import SignUpView

urlpatterns = [
    path("account/", SignUpView.as_view()),
]