from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()
    context = {'job_list': job_list}

    return render (request, 'job/job_list.html', context=context)

def job_details(request, id):
    job_details = Job.objects.get(id=id)
    context={'job': job_details}

    return render(request, 'job/job_detail.html',context=context)