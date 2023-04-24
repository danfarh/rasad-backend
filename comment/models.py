from django.db import models
from users.models import CustomUser
from product.models import Product 


class Question(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True,blank=True)
    text = models.TextField()
    confirm = models.BooleanField(default=False)
    def __str__(self):
	    return self.title


class Answer(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.TextField()
    confirm = models.BooleanField(default=False)
    def __str__(self):
	    return self.text
