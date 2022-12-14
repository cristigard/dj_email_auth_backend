from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.CustomUserRegisterView.as_view(), 
    		name='register'),
    path('login/', views.CustomUserLoginView.as_view(), 
    		name='login'),
    path('logout/', auth_views.LogoutView.as_view(), 
    		name = 'logout'),
    path('password_change/', views.CustomUserChangePassView.as_view(), 
    		name = 'password_change'),
    path('password_change_done/', views.CustomUserChangePassDoneView.as_view(), 
    		name = 'password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'), 
         	name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'),
         	name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html'),
         	name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'),
         	name='password_reset_complete'),
]
