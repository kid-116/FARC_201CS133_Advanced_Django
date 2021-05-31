from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from sections.models import Section

@login_required(login_url='accounts:login_path')
def home(request):
    return render(request, 'sections/home.html', {
        'id_s': request.user.section
    })

