from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from main.views import RegisterUser
from main.views import LoginUser
from main.views import LogoutUser



urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutUser, name="logout"),
    path("about/", views.about, name="about"), #также можно написать include('about.urls') чтобы когда пользователь 
    path("", views.index, name="index"),       #переходил по url /about/что-то_еще, то это будет обраб-ся в about.urls
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
