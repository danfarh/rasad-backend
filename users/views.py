from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.response import Response
from .models import CustomUser as User, Company, Activity
from category.models import Category
from .serializers import (RegisterSerializer,
                        LoginSerializer,
                        CompanySerializer,
                        CreateCompanySerializer,
                        VisitorSerializer,
                        ReportVisitorsActivitySerializer,
                        VisitorCoordinatesSerializer,)
from utils.token import get_tokens_for_user
from django.contrib.auth.hashers import make_password,check_password
from utils.permissions import IsBoss,IsVisitor
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate,login


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User(
            first_name=serializer.data.get('first_name'),
            last_name=serializer.data.get('last_name'),
            email=serializer.data.get('email'),
            phone_number=serializer.data.get('phone_number'),
            password=make_password(serializer.data.get('password')),
            user_type=serializer.data.get('user_type')
            )
            user.save()
            token = get_tokens_for_user(user=user)
            print(serializer.data)
            return Response({"token": token}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.data.get('phone_number', None)
            password = serializer.data.get('password', None)
            password = password.rstrip("\n")
            user = get_object_or_404(User, phone_number=phone_number)
            match_password = check_password(password, user.password)
            if user and match_password:
                token = get_tokens_for_user(user=user)
                print(request.user)     
                return Response({"token": token}, status=status.HTTP_200_OK)   
            else:
                return Response('User not found!', status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)        


class CreateCompanyView(generics.GenericAPIView):
    permission_classes = (IsBoss, )
    serializer_class = CreateCompanySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.user)
            category = get_object_or_404(Category, pk=serializer.data.get('category'))
            try:
                company = Company(
                name=serializer.data.get('name'),
                image=request.FILES['image'],
                category=category,
                boss_id=request.user
                )
                company.save()
            except:
                company = Company(
                name=serializer.data.get('name'),
                category=category,
                boss_id=request.user
                )
                company.save()    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AddVisitorByBossView(generics.GenericAPIView):
    permission_classes = (IsBoss, )
    serializer_class = VisitorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            visitor = User(
            first_name=serializer.data.get('first_name'),
            last_name=serializer.data.get('last_name'),
            phone_number=serializer.data.get('phone_number'),
            password=make_password(serializer.data.get('password')),
            user_type='V',
            boss_id=request.user,
            center_x=serializer.data.get('center_x'),
            center_y=serializer.data.get('center_y'),
            radius=serializer.data.get('radius'),
            )
            visitor.save()

            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListVisitorsView(generics.ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class = VisitorSerializer 

    def get_queryset(self):
        visitors = User.objects.filter(user_type='V',boss_id=self.request.user)
        return visitors      

	  
class RetrieveUpdateDestroyVisitorView(generics.RetrieveUpdateDestroyAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class = VisitorSerializer
    def get_queryset(self):
        queryset = User.objects.filter(user_type='V',boss_id=self.request.user)
        return queryset


class ListCompanyView(generics.ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer

    def get_queryset(self):
        companies = Company.objects.filter(boss_id=self.request.user)
        return companies


#report
class ReportVisitorsActivity(generics.GenericAPIView):
    permission_classes = [IsBoss]
    serializer_class = ReportVisitorsActivitySerializer
    def get(self, request, company_id):
        hours_of_work = 0
        sales_amount = 0
        num_out_of_limit = 0
        get_object_or_404(Company, pk=company_id,boss_id=request.user)
        visitors = User.objects.filter(user_type='V',boss_id=request.user)
        report = []
        
        for visitor in visitors:
            activities = Activity.objects.filter(visitor_id=visitor)
            for activity in activities:
                hours_of_work += activity.hours_of_work
                sales_amount += activity.sales_amount
                num_out_of_limit += activity.num_out_of_limit
            report.append({
                "visitor": visitor.last_name,
                "hours_of_work": hours_of_work,
                "sales_amount": sales_amount,
                "num_out_of_limit": num_out_of_limit
            })  
            hours_of_work = 0
            sales_amount = 0
            num_out_of_limit = 0       
          
        return Response({"data": report}, status=status.HTTP_201_CREATED)      


class GetVisitorCoordinates(generics.ListAPIView):
    permission_classes = [IsVisitor]
    serializer_class = VisitorCoordinatesSerializer

    def get_queryset(self):
        queryset = User.objects.filter(pk=self.request.user.pk)
        return queryset


class GetVisitorActivity(generics.GenericAPIView):
    permission_classes = [IsVisitor]
    serializer_class = ReportVisitorsActivitySerializer
    def get(self, request):
        hours_of_work = 0
        sales_amount = 0
        num_out_of_limit = 0

        visitor = get_object_or_404(User, pk=request.user.pk)

        report = []
        activities = Activity.objects.filter(visitor_id=visitor)

        for index,activity in enumerate(activities):
            hours_of_work += activity.hours_of_work
            sales_amount += activity.sales_amount
            num_out_of_limit += activity.num_out_of_limit
            report.append({
                "day": index + 1,
                "hours_of_work": hours_of_work,
                "sales_amount": sales_amount,
                "num_out_of_limit": num_out_of_limit
            })  
            hours_of_work = 0
            sales_amount = 0
            num_out_of_limit = 0       
          
        return Response({"data": report}, status=status.HTTP_201_CREATED)  