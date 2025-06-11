from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from users import views
from users.views import RegisterUser
from users.views import LoginUser
from users.views import LogoutUser

urlpatterns = [
    path("", views.users, name="users"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutUser, name="logout"),
    # path('profile/', views.profile_view, name='profile'),
    path("profile/<int:profile_id>/", views.profile_view, name="user_page"),
]
