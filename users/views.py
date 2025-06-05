from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from users.forms import RegisterUserForm
from users.forms import LoginUserForm
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm
from main.utils import DataMixin
from django.contrib.auth import logout
from django.contrib.auth import login

def index(request) -> HttpResponse:
    return render(request, "main/index.html")

def about(request) -> HttpResponse:
    return render(request, "main/index.html")

def users(request) -> HttpResponse:
    return render(request, "users/login.html")

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy("index")
    # В settings.py указан параметр LOGIN_REDIRECT_URL = 'index' в таком случае в данной функции нет нужды


def LogoutUser(request):
    logout(request)
    return redirect('index')