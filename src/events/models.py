from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_attendees(self):
        return ', '.join([str(i) for i in self.events_date.all()])


class Attendee(models.Model):
    name = models.CharField(max_length=25)
    registration_date = models.ManyToManyField(Event, related_name='events_date')

    def __str__(self):
        return f'{self.name}'

