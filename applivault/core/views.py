from django.shortcuts import render

from job.models import Job

from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect



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
                Q(job_name__icontains=query) | 
                Q(job_poster__username__icontains=query) |
                Q(company_name__icontains=query) |
                Q(company_website_link__icontains=query) |
                Q(job_alternative_location__icontains=query) |
                Q(experience_level__icontains=query) |
                Q(job_type__icontains=query) |
                Q(job_details__icontains=query)|
                Q(job_salary__icontains=query)
                )
            return render(request, "core/search_jobs.html", {
                'jobs': jobs,
                })

    jobs = Job.objects.all()
    return render(request, "core/search_jobs.html", {
        'jobs': jobs,
    })

def job_details(request, pk):
    job = get_object_or_404(Job, pk=pk)

    return render(request, "core/job_details.html", {
        'job': job,
        'pk': pk,
    })
