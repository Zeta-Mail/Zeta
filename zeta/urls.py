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
    path("reply", views.reply, name="reply"),
    path("compose", views.compose, name="compose"),
    path("folder_create_page", views.folder_create_page, name="folder_create_page"),
    path("contact_us", views.contact_us, name="contact_us"),
]