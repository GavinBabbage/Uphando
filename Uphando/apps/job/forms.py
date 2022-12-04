from django import forms

from .models import Job

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        # fields = ['title', 'short_description', 'long_description', 'Name_of_Researcher', 'Remuneration', 'company_zipcode', 'Ethic_Disclaimer', 'company_country', 'company_size', 'deadline']
        fields = ['title', 'short_description', 'long_description', 'Name_of_Researcher', 'Remuneration', 'Ethic_Disclaimer', 'Contact_Details', 'deadline']

