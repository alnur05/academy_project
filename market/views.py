from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from market.models import Course, CourseForUser2


def show_courses(request: HttpRequest) -> HttpResponse:
    global course_available
    user = request.user
    if not user.is_authenticated:
        return redirect("/login")
    # if CourseForUser2.object == user.username:
    #     course_available = "avail"
    # else:
    #     course_available = "not avail"

    context = {
        "courses": Course.objects.all(),
        "CoursesForUser2": CourseForUser2.objects.all(),
        "username": user.username
    }
    return render(request, "index.html", context)


def show_course(request: HttpRequest) -> HttpResponse:
    return render(request, "course.html")
