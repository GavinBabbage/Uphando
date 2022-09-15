from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from apps.job.models import Job

def frontpage(request):
    jobs = Job.objects.order_by('-created_at')
    print(jobs)

    return render(request, 'core/frontpage.html', {'jobs': jobs})

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('job')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'core/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})
