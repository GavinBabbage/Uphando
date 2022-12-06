from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . import api
from .forms import AddJobForm
from .models import Job


def search(request):
    return render(request, 'job/search.html')


def all_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'job/all_jobs.html', {'jobs': jobs})


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, "Notice posted successfully.")

            return redirect('frontpage')
    else:
        form = AddJobForm()

    return render(request, 'job/add_job.html', {'form': form})


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'job/job_detail.html', {'job': job})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            messages.success(request, "Notice edited successfully.")
            return redirect('frontpage')
    else:
        form = AddJobForm(instance=job)

    return render(request, 'job/edit_job.html', {'form': form, 'job': job})


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)
    job.delete()
    messages.success(request, "Notice successfully deleted.")
    return redirect('frontpage')
