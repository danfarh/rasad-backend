from django.db import models
from datetime import datetime
from users.models import Company
from category.models import Category
# Create your models here.


def product_image_path(instance, filename):
    now = datetime.now()
    return 'products/image/{0}/{1}/{2}/image_{3}/{4}'.format(
        now.strftime("%Y"),
        now.strftime("%m"),
        now.strftime("%d"),
		instance.id,
        filename)

class Product(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=product_image_path,null=True,blank=True)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    category = models.ForeignKey(
		Category,
		on_delete=models.SET_NULL,
		null=True,
		related_name='products'
	)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name









    


	
    
	
      