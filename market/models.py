from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.id}: {self.name}"

class CourseForUser(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.name}, {self.user_id}"


class CourseForUser2(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    user_name = models.CharField(max_length=255, blank=False, null=False)
    user_id = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.id}: {self.name}, {self.user_name}, {self.user_id}"