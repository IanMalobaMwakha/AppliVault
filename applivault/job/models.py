from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Job(models.Model):
    job_name = models.CharField(max_length=125)
    job_poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_website_link = models.CharField(max_length=500, blank=True, null=True)
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
    job_details = models.TextField(null=True, blank=True)
    job_application_link = models.CharField(max_length=125, blank=True, null=True)

    def __str__(self):
        return self.job_name