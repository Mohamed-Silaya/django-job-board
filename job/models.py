from django.db import models

# Create your models here.

'''
 Django model field :
    - for html widget
    - for validation
    - for database size
'''
JOB_TYPE =(
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('contract', 'Contract'),
    ('temporary', 'Temporary'),
    ('internship', 'Internship'),
    ('volunteer', 'Volunteer'),
    ('remote', 'Remote'),
    ('freelance', 'Freelance')
)


class Job (models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category= models.ForeignKey('Category',on_delete=models.CASCADE) 
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Category (models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


