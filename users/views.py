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
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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



from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)







# class UserProfileView(TemplateView):  
#     template_name = 'user_app/profile_page.html'  

#     def get_context_data(self, **kwargs):  
#         context = super().get_context_data(**kwargs)  
#         try:  
#             user = get_object_or_404(User, username=self.kwargs.get('username'))  
#         except User.DoesNotExist:  
#             raise Http404("Пользователь не найден")  
#         context['user_profile'] = user  
#         context['title'] = f'Профиль пользователя {user}'  
#         return context
    

