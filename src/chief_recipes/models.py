from django.db import models


class Chief(models.Model):
    name = models.CharField(max_length=30)
    experience = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=40)
    cuisine = models.CharField(max_length=30)
    chief = models.ForeignKey(to=Chief, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
