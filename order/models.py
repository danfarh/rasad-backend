from django.db import models
from product.models import Product
from users.models import CustomUser as User
from cart.models import Item


class Order(models.Model):
    state_choices = (
        ("p" , "pending"),
        ("i" , "in-progress"),
        ("d" , "delivered"),
        ("r" , "returned"),
        ("c" , "canceled")
    )
    deliverMethod_choices =(
        ("e","express"),
        ("p","post")
    )
    paymentMethod_choices =(
        ("o" , "online"),
        ("c" , "cash")
    )
    amount = models.FloatField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(choices=state_choices,max_length=1) 
    deliverMethod = models.CharField(choices=deliverMethod_choices,max_length=1)
    paymentMethod = models.CharField(choices=paymentMethod_choices,max_length=1)
    items = models.ManyToManyField(Item,blank=True,null=True,related_name='items')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}-{self.user.phone_number}'


class OfflineOrder(models.Model):
    visitor_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'visitor-{self.visitor_id.phone_number}_product-{self.product_id}'