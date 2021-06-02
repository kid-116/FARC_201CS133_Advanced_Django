from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lectures.models import Lecture

@login_required(login_url='accounts:login_path')
def home(request):
    section = request.user.section
    lectures = None
    events = None
    if section:
        events = section.events.order_by('starts_at')
        order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        qs = Lecture.objects.filter(section=section).order_by('starts_at')
        lectures = sorted(qs, key=lambda l: order.index(l.day))

    return render(request, 'sections/home.html', {
        'section': section,
        'lectures': lectures,
        'events': events,    
    })

