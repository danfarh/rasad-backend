from django.urls import path
from . import views

app_name='categories'
urlpatterns = [
    path('', views.ListCompanyCategoriesView.as_view() , name='categories'), 
]