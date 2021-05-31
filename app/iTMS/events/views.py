from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import EventCreationForm
from .models import Event

@login_required(login_url='accounts:login_path')
def create(request):
    if request.user.section and request.user.is_cr:    
        if request.method == 'POST':
            form = EventCreationForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.section = request.user.section
                event.save()
                return redirect('sections:home_path')
        else:
            form = EventCreationForm()
        return render(request, 'events/create.html', { 'form': form })
    else:
        raise PermissionError

@login_required(login_url='accounts:login_path')
def edit(request, id_e):
    if request.user.section and request.user.is_cr:
        event = Event.objects.get(pk=id_e)
        form = EventCreationForm(request.POST or None, instance=event)
        if form.is_valid():
            form.save()
            return redirect('sections:home_path')
        return render(request, 'events/update.html', { 'form': form, 'event': event })
    else:
        raise PermissionError

@login_required(login_url='accounts:login_path')
def delete(request, id_e):
    if request.user.section and request.user.is_cr:
        Event.objects.get(pk=id_e).delete()
        return redirect('sections:home_path')
    else:
        raise PermissionError

