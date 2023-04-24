from django.urls import path
from . import views

app_name='jobs'
urlpatterns = [
    #retrieve & create & list jobs
    path('job/', views.ListJobView.as_view() , name='jobs'), 
    path('job/create/', views.CreateJobView.as_view() , name='create_job'), 
    path('job/<int:pk>/', views.RetrieveJobView.as_view() , name='job'),
   
    #retrieve & create & list resumes
    path('resume/', views.ListResumeView.as_view() , name='resumes'), 
    path('resume/send/', views.SendResumeView.as_view() , name='create_resume'), 
    path('resume/<int:pk>/', views.RetrieveResumeView.as_view() , name='resume'),
   
]