from datetime import date
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Job(models.Model):
    job_name = models.CharField(max_length=125)
    job_poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    
    skills = models.ListField(default=list, blank=True)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            self.save()

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            self.save()

    def clear_skills(self):
        self.skills = []
        self.save()