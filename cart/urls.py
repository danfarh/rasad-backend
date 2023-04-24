from django.urls import path
from . import views

app_name='carts'
urlpatterns = [
    path('add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('get/', views.GetCartView.as_view(), name='get_cart'),
    path('get/price/', views.GetTotalCartPriceView.as_view(), name='get_total_cart_price'),
]