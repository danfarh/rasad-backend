from django.urls import path
from . import views

app_name='orders'
urlpatterns = [
    path('', views.ListOrderView.as_view() , name='orders_list'),
    path('create/', views.CreateOrderView.as_view() , name='orders_create'),
    path('<int:pk>/', views.RetrieveUpdateDestroyOrderView.as_view() , name='orders_listCreate'),
    path('create/visitor/', views.CreateOfflineOrderView.as_view() , name='order_create_by_visitor'),
]