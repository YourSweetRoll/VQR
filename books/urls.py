from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from books import views


urlpatterns = [
    path("", views.book_list, name="books"),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    path('create/', views.create_book, name='create_book'),
    path('<int:book_id>/create_chapter/', views.create_chapter, name='create_chapter'),
]
