from django.shortcuts import render

from job.models import Job

from django.db.models import Q


def index(request):
    jobs = Job.objects.all()

    return render(request, "core/index.html", {
        'jobs': jobs,
    })

def search(request):

    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            jobs = Job.objects.filter(
                Q(job_name__icontains=query) | Q(job_details__icontains=query)
                )
            return render(request, "core/search_jobs.html", {
                'jobs': jobs,
                })

    jobs = Job.objects.all()
    return render(request, "core/search_jobs.html", {
        'jobs': jobs,
    })

