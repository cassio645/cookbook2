from django.urls import path

from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [ 
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro/", views.SignupView.as_view(), name="cadastro"),

    path("password_reset/", 
        auth_views.PasswordResetView.as_view(template_name="senha/password_reset_form.html"),
        name="reset_password"),

    path("password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="senha/password_reset_done.html"),
        name="password_reset_done"),

    path("reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="senha/password_reset_confirm.html"),
        name="password_reset_confirm"),

    path("reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="senha/password_reset_complete.html"),
        name="password_reset_complete"),
]