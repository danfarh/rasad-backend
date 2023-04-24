from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('', views.ListProductView.as_view() , name='products'),
    path('create/', views.CreateProductView.as_view() , name='create_product'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProductView.as_view() , name='product'),
]