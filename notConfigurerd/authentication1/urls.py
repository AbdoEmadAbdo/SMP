 
from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="S_IN"),
    path('register/', register_user, name="signUp"),
    path("logout/", LogoutView.as_view(), name="logout")
]
