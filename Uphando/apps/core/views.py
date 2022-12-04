from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
import datetime
from django.utils import timezone

from apps.job.models import Job

def frontpage(request):
    jobs = Job.objects.all()

    # print(jobs)
    for job in jobs:
        # if(job.deadline<datetime.date.today()):
        if (job.deadline < timezone.now()):
            job.delete()
        else:
            jobs = Job.objects.order_by('-created_at')

    return render(request, 'core/frontpage.html', {'jobs': jobs})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
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
            messages.success(request, "Signup successful.")
            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})