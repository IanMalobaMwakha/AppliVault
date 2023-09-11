from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from datetime import date, datetime


class Job(models.Model):
    job_name = models.CharField(max_length=125)
    job_poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateField(auto_now_add=True)

    EXPERIENCE_LEVEL_CHOICES = (
        ('Internship', 'Internship'),
        ('Entry Level', 'Entry Level'),
        ('Associate', 'Associate'),
        ('Mid-Senior Level', 'Mid-Senior Level'),
        ('Senior Level', 'Senior Level'),
        ('Director', 'Director'),
        ('Executive', 'Executive')
    )
    experience_level = MultiSelectField(max_length=125, choices=EXPERIENCE_LEVEL_CHOICES)

    def __str__(self):
        return self.job_name + " | " + str(self.job_poster)

