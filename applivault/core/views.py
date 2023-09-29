from django.shortcuts import render

from job.models import Job

def index(request):
    jobs = Job.objects.all()

    return render(request, "core/index.html", {
        'jobs': jobs,
    })

def search(request):
    jobs = Job.objects.all()
    return render(request, "core/search_jobs.html", {
        'jobs': jobs,
    })