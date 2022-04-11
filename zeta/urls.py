from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("email_body", views.email_body, name="email_body"),
    path("privacy_page", views.privacy_page, name="privacy_page"),
    path("about_us", views.about_us, name="about_us"),
]