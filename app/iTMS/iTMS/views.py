from django.shortcuts import render, redirect

def landing(request):
    if request.user.is_authenticated:
        return redirect('sections:home_path')
    return render(request, 'landing.html')