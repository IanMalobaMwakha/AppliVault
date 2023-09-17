from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django_ckeditor_5.fields import CKEditor5Field


class Job(models.Model):
    job_name = models.CharField(max_length=125)
    job_poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_website_link = models.CharField(max_length=500, blank=True, null=True)
    job_location = CountryField(blank_label="(Select Countries)",multiple=True, blank=True)
    job_alternative_location = models.CharField(max_length=250, blank=True, null=True)
    EXPERIENCE_LEVEL_CHOICES = (
        ('Internship', 'Internship'),
        ('Entry Level', 'Entry Level'),
        ('Associate', 'Associate'),
        ('Mid-Senior Level', 'Mid-Senior Level'),
        ('Senior Level', 'Senior Level'),
        ('Director', 'Director'),
        ('Executive', 'Executive')
    )
    experience_level = MultiSelectField(max_length=125, choices=EXPERIENCE_LEVEL_CHOICES, blank=True)

    JOB_TYPE_CHOICES = (
        ('Remote', 'Remote'),
        ('On-site', 'On-site'),
        ('Hybrid', 'Hybrid')
    )
    job_type = MultiSelectField(max_length=125, choices=JOB_TYPE_CHOICES, blank=True)
    job_details = CKEditor5Field(null=True, blank=True)
    job_salary = models.CharField(max_length=100, blank=True, null=True)
    job_application_link = models.CharField(max_length=125, blank=True, null=True)

    def __str__(self):
        return self.job_name
    
    