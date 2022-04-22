from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def index(request):
        return render(request, "zeta/index.html")

def home(request):
        return render(request, "zeta/home.html")


def email_body(request):
        return render(request, "zeta/email_body.html")

def privacy_page(request):
        return render(request, "zeta/privacy_page.html")

def about_us(request):
        return render(request, "zeta/about_us.html")

def reply(request):
        return render(request, "zeta/reply.html")

def compose(request):
        return render(request, "zeta/compose.html")

def folder_create_page(request):
        return render(request, "zeta/folder_create_page.html")

def contact_us(request):
    return render(request, "zeta/contact_us.html")

def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "zeta/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "zeta/login.html")

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "zeta/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "zeta/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "zeta/register.html")