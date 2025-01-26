from django.contrib.auth import views as auth_views
from django.urls import path

from gym import views
from gym import forms

urlpatterns = [
    path("", views.homepage, name= "homepage"),
    path("login/", auth_views.LoginView.as_view (template_name="gym/login.html", authentication_form=forms.CustomAuthenticationForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path("update_goals/", , name="update_goals"),
    path("log_workout/", views.log_workout, name="log_workout"),
    path("create_workout_preset/", views.create_workout_preset, name="create_workout_preset"),
    # path("view_stats/", , name="view_stats"),
    # path("view_progress/", , name="view_progress"),
]