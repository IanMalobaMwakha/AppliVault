from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Job(models.Model):
    job_name = models.CharField(max_length=125)

    EXPERIENCE_LEVEL_CHOICES = (
        ('Internship', 'Internship'),
        ('Entry Level', 'Entry Level'),
        ('Associate', 'Associate'),
        ('Mid-Senior Level', 'Mid-Senior Level'),
        ('Senior Level', 'Senior Level'),
        ('Director', 'Director'),
        ('Exercutive', 'Exercutive')
    )
    experience_level = MultiSelectField(max_length=125, choices=EXPERIENCE_LEVEL_CHOICES)

    def __str__(self):
        return self.job_name

