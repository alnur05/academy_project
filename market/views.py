from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def show_courses(request: HttpRequest) -> HttpResponse:
    user = request.user
    if not user.is_authenticated:
        return redirect("/login")
    return render(request, "index.html")


def show_course(request: HttpRequest) -> HttpResponse:
    return render(request, "course.html")
