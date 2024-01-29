from django.shortcuts import render
from .models import Event
from django.utils.timezone import now


def countdown_timer(request):
    title = Event.objects.first()
    data = Event.objects.first().event_date
    t_now = str(now()).split(' ')[1].split('.')[0]
    t_event = str(data).split(' ')[1].split('+')[0]
    hour_n, minute_n, second_n = t_now.split(':')
    hour_e, minute_e, second_e = t_event.split(':')
    hour = int(hour_e) - int(hour_n)
    minute = int(minute_e) - int(minute_n)
    seconds = int(second_e) - int(second_n)
    context = {'hours': hour, 'minutes': minute, 'seconds': seconds, 'data': title}
    return render(request, 'myapp.html', context)