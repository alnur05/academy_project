from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Проверяем, есть ли такой bad user
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html", context={"message": "Wrong username or password"})

        # Если есть, то записываем в Cookie номер пользователя (id)
        login(request, user)
        return HttpResponseRedirect("/")

    return render(request, "login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    # Чистим Cookie
    logout(request)
    return HttpResponseRedirect("/")
