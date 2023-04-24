from rest_framework import generics,status

from users.models import Company
from .models import Question,Answer
from product.models import Product
from .serializers import (CreateQuestionSerializer,QuestionSerializer,AnswerSerializer,CreateAnswerSerializer)
from utils.permissions import IsCustomer,IsBoss
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


#######question by customer
class RetrieveQuestionView(generics.RetrieveAPIView): 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
  

class ListQuestionView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)  
    serializer_class = QuestionSerializer
    filterset_fields = ['user','product','confirm']

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.request.data.get('product'))
        company = get_object_or_404(Company, pk=product.company.id)
        question = Question.objects.filter(product__company=company)
        return question


class CreateQuestionView(generics.GenericAPIView):
    permission_classes = (IsCustomer,)  
    serializer_class = CreateQuestionSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.user)
            product = get_object_or_404(Product, pk=serializer.data.get('product'))
            question = Question(
            text=serializer.data.get('text'),
            title=serializer.data.get('title'),
            user=request.user,
            product=product
            )
            question.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#######answer by boss
class RetrieveAnswerView(generics.RetrieveAPIView): 
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
     

class ListAnswerView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filterset_fields = ['user','question','confirm']


class CreateAnswerView(generics.GenericAPIView):
    permission_classes = (IsBoss,)  
    serializer_class = CreateAnswerSerializer 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print(request.user)
            question = get_object_or_404(Question, pk=serializer.data.get('question'))
            answer = Answer(
            text=serializer.data.get('text'),
            question=question,
            user=request.user
            )
            answer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
