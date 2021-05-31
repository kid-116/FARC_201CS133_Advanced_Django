from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import LectureCreationForm
from .models import Lecture

@login_required(login_url='accounts:login_path')
def create(request):
    if request.user.section and request.user.is_cr:    
        if request.method == 'POST':
            form = LectureCreationForm(request.POST)
            if form.is_valid():
                lecture = form.save(commit=False)
                lecture.section = request.user.section
                lecture.save()
                return redirect('sections:home_path')
        else:
            form = LectureCreationForm()
        return render(request, 'lectures/create.html', { 'form': form })
    else:
        raise PermissionError

@login_required(login_url='accounts:login_path')
def edit(request, id_l):
    if request.user.section and request.user.is_cr:
        lecture = Lecture.objects.get(pk=id_l)
        form = LectureCreationForm(request.POST or None, instance=lecture)
        if form.is_valid():
            form.save()
            return redirect('sections:home_path')
        return render(request, 'lectures/edit.html', { 'form': form, 'lecture': lecture })
    else:
        raise PermissionError

@login_required(login_url='accounts:login_path')
def delete(request, id_l):
    if request.user.section and request.user.is_cr:
        Lecture.objects.get(id=id_l).delete()
        return redirect('sections:home_path')
    else:
        raise PermissionError