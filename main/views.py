from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    return render(request, "main/index.html")


def registration(request) -> HttpResponse:
    return render(request, "accounts/reg/signup.html")
