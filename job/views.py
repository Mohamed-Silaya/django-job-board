from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    job_list = Job.objects.all()

    return render ()

def job_details(request, id):
    pass