from rest_framework import serializers
from .models import Job,Resume
from users.serializers import CompanySerializer,RegisterSerializer


class JobSerializer(serializers.ModelSerializer):
    company_id = CompanySerializer()
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company_id', 'salary', 'active']        


class CreateJobSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField()
    title = serializers.CharField(required=True)
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'company_id', 'salary', 'active']   


class ResumeSerializer(serializers.ModelSerializer):
    visitor_id = RegisterSerializer()
    job_id = JobSerializer()
    class Meta:
        model = Resume
        fields = ['id', 'title', 'description', 'job_id', 'visitor_id', 'resume']    


class SendResumeSerializer(serializers.ModelSerializer):
    job_id = serializers.IntegerField()
    title = serializers.CharField(required=True)
    class Meta:
        model = Resume
        fields = ['id', 'title', 'description', 'job_id', 'resume']          