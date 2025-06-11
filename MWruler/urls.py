from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include('users.urls')),
    path("books/", include('books.urls')),
    path("about/", include('main.urls')), #также можно написать include('about.urls') чтобы когда пользователь 
    path("", include('main.urls')),       #переходил по url /about/что-то_еще, то это будет обраб-ся в about.urls
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
