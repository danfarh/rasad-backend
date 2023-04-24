from django.urls import path
from . import views

app_name='comments'
urlpatterns = [
    #retrieve & create & list questions
    path('question/', views.ListQuestionView.as_view() , name='questions'), 
    path('question/create/', views.CreateQuestionView.as_view() , name='create_question'), 
    path('question/<int:pk>/', views.RetrieveQuestionView.as_view() , name='question'),
   
    #retrieve & create & list answers
    path('answer/', views.ListAnswerView.as_view() , name='answers'), 
    path('answer/create/', views.CreateAnswerView.as_view() , name='create_answer'), 
    path('answer/<int:pk>/', views.RetrieveAnswerView.as_view() , name='answer'),
   
]