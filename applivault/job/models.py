from django.db import models

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
    experience_level = models.CharField(max_length=100, choices=EXPERIENCE_LEVEL_CHOICES)

    