from django.shortcuts import render
from .models import Event
from django.views.generic import View


class EventView(View):
    def get(self, request):
        events = Event.objects.all()
        return render(request, 'events/index.html', context={'events': events})

