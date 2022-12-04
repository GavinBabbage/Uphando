from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    Name_of_Researcher = models.CharField(max_length=255)
    Remuneration = models.CharField(max_length=255, blank=True, null=True)
    Ethic_Disclaimer = models.CharField(max_length=255, blank=True, null=True)
    Contact_Details = models.CharField(max_length=255, blank=True, null=True)
    deadline = models.DateTimeField(null=True)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
