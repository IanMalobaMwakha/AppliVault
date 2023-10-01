from django.shortcuts import render

from job.models import Job

def index(request):
    jobs = Job.objects.all()

    return render(request, "core/index.html", {
        'jobs': jobs,
    })

def search(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            jobs = Job.objects.filter(job_name__icontains=query)
            return render(request, "core/search_jobs.html", {
                'jobs': jobs,
                })

    jobs = Job.objects.all()
    return render(request, "core/search_jobs.html", {
        'jobs': jobs,
    })

