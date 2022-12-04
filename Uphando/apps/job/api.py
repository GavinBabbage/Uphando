import json

from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from .models import Job


def api_search(request):
        jobslist = []
        data = json.loads(request.body)
        query = data['query']

        jobs = Job.objects.filter(Q(title__icontains=query) | Q(short_description__icontains=query) | Q(long_description__icontains=query) | Q(Name_of_Researcher__icontains=query) | Q(Ethic_Disclaimer__icontains=query) | Q(Remuneration__icontains=query) | Q(deadline__icontains=query) | Q(Contact_Details__icontains=query))

        for job in jobs:
            obj = {
                'id': job.id,
                'title': job.title,
                'Name_of_Researcher': job.Name_of_Researcher,
                'url': '/jobs/%s/' % job.id
            }
            jobslist.append(obj)

        return JsonResponse({'jobs': jobslist})
