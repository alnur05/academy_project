from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from market.models import Course, CourseForUser


def show_courses(request: HttpRequest) -> HttpResponse:
    user = request.user
    if not user.is_authenticated:
        return redirect("/login")
    course_available = CourseForUser(user_id=user.id).all()
    context = {
        "courses": Course.objects.all(),
        "CoursesForUser": CourseForUser.objects.all(),
        "course_available": course_available,
        "user_id": user.id
    }
    return render(request, "index.html", context)


def show_course(request: HttpRequest) -> HttpResponse:
    return render(request, "course.html")
