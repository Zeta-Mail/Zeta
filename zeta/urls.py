from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("spam", views.spam, name="spam"),
    path("trash", views.trash, name="trash"),
    path("important", views.important, name="important"),
    path("loading", views.loading, name="loading"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("email/<str:email_id>", views.email, name="email"),
    path("privacy", views.privacy, name="privacy"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("reply", views.reply, name="reply"),
    path("compose", views.compose, name="compose"),
    path("create", views.create, name="create"),
]