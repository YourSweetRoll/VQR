from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from main import views
from .views import RegisterUser

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("register/", RegisterUser.as_view(), name="register"),   #нужно подумать над views.register
    # path("", login, name="login"),
]