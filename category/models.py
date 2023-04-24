from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('P','Product'),
        ('C','Compay')
    )
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    title = models.CharField(max_length=200, verbose_name='title')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')
    status = models.BooleanField(default=True, verbose_name='status')
    type   = models.CharField(max_length=1,choices=CATEGORY_CHOICES,default='P')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 

    def __str__(self):
        return self.title