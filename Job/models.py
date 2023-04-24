from django.db import models
from users.models import (Company,CustomUser)

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    salary = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs' 

    def __str__(self):
	    return self.title   

class Resume(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    job_id = models.ForeignKey(Job,on_delete=models.CASCADE)
    visitor_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    resume = models.FileField()
    create_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes' 

    def __str__(self):
	    return self.title  