from django.urls import path

from users.views import UserView, LoginView

urlpatterns = [
    path("account/", UserView.as_view()),
    path("login/", LoginView.as_view())
]