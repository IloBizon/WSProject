from django.db import models


class Athlete(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField(default=18)
    nationality = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Record(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    athlete = models.OneToOneField(to=Athlete, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
