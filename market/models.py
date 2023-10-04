from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    available = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, default="")

    # def cars_left(self) -> int:
    #     ordered = Order.objects.filter(car=self).count()
    #     purchased = 0
    #     for purchase in Purchase.objects.filter(car=self):
    #         purchased += purchase.count
    #     return purchased - ordered

    def __str__(self):
        return f"{self.id}: {self.name}, available: {self.available}"
