from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.job.models import Job, Application
from apps.notification.utilities import create_notification
from django.contrib import messages

# Create your views here.