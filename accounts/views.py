
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import CustomRegisterForm, CustomAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin




class CustomUserRegisterView(generic.CreateView):
    form_class = CustomRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
  

class CustomUserLoginView(auth_views.LoginView):
	form_class = CustomAuthenticationForm
	template_name = 'accounts/login.html'

class CustomUserLogoutView(LoginRequiredMixin, auth_views.LogoutView):
	next_page = 'login'


class CustomUserChangePassView(LoginRequiredMixin, auth_views.PasswordChangeView):  
	form_class = PasswordChangeForm
	template_name = 'accounts/password_change_form.html'
	success_url = reverse_lazy('password_change_done')

class CustomUserChangePassDoneView(LoginRequiredMixin, auth_views.PasswordChangeDoneView):
	template_name = 'accounts/password_change_done.html'