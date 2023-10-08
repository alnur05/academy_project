from django.contrib import admin
from market.models import Course, CourseForUser, CourseForUser2
admin.site.register(Course)
admin.site.register(CourseForUser)
admin.site.register(CourseForUser2)
# Register your models here.