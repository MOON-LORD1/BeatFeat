from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(req):
    return render(req, "index.html")

def login_user(req):
    if req.method == 'POST':
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect("index")
        else:
            return HttpResponse("<h1>Данного аккаунта не существует</h1><a href='{% url 'index' %}'>На главную</a>")
    else:
        return render(req, "index.html")

def logout_user(req):
    logout(req)
    return redirect("index")

def register_user(req):
    if req.method == 'POST':
        username = req.POST["username"]
        password = req.POST["password"]
        email = req.POST["email"]

        user = User.objects.filter(username=username).first()

        if user is None:
            created_user = User.objects.create_user(username=username, email=email, password=password)
            login(req, user=created_user)
            return redirect("index")
        else:
            return HttpResponse("Вы уже зарегистрированы")
    else:
        return render(req, "index.html")
