from django.urls import path, include

from users.views import UserView

urlpatterns = [
    path("account/", UserView.as_view()),
]