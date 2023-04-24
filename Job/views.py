from rest_framework import generics,status
from users.models import Company
from .models import Job,Resume
from .serializers import (CreateJobSerializer,JobSerializer,ResumeSerializer,SendResumeSerializer)
from utils.permissions import IsVisitor,IsBoss
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


#######job 
class RetrieveJobView(generics.RetrieveAPIView): 
    queryset = Job.objects.all()
    serializer_class = JobSerializer
  

class ListJobView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filterset_fields = ['active','company_id']


class CreateJobView(generics.GenericAPIView):
    permission_classes = (IsBoss,)  
    serializer_class = CreateJobSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.user)
            company = get_object_or_404(Company, pk=serializer.data.get('company_id'), boss_id=request.user)
            job = Job(
            title=serializer.data.get('title'),
            description=serializer.data.get('description'),
            salary=serializer.data.get('salary'),
            company_id=company
            )
            job.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#######resume 
class RetrieveResumeView(generics.RetrieveAPIView): 
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
     

class ListResumeView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filterset_fields = ['job_id','visitor_id']


class SendResumeView(generics.GenericAPIView):
    permission_classes = (IsVisitor,)  
    serializer_class = SendResumeSerializer 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.user)
            job = get_object_or_404(Job, pk=serializer.data.get('job_id'))
            try:
                resume = Resume(
                title=serializer.data.get('title'),
                description=serializer.data.get('description'),
                resume=request.FILES['resume'],
                job_id=job,
                visitor_id=request.user
                )
                resume.save()
            except:
                resume = Resume(
                title=serializer.data.get('title'),
                description=serializer.data.get('description'),
                job_id=job,
                visitor_id=request.user
                )
                resume.save()    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
