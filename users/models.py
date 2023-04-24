from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _  
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import datetime
from category.models import Category
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManger                                 


def phone_validate(value):
    if len(value) != 11:
        raise ValidationError(
            _('%(value)s Phone number must be an 11 character'),
            params={'value': value},
        )
    if not value.isnumeric():
         raise ValidationError(
            _('%(value)s Phone number must be a number'),
            params={'value': value},
        )

def company_image_path(instance, filename):
    now = datetime.now()
    return 'companies/image/{0}/{1}/{2}/image_{3}/{4}'.format(
        now.strftime("%Y"),
        now.strftime("%m"),
        now.strftime("%d"),
		instance.id,
        filename)

class CustomUser(AbstractBaseUser):
    TYPE_CHOICES = (
        ('B','Boss'),
        ('V','Visitor'),
        ('C','Customer')
    )
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name  = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=60, unique=True,null=True)
    phone_number = models.CharField(max_length=15, unique=True,null=True, validators=[phone_validate])
    password = models.CharField(max_length=100,validators=[MinLengthValidator(8)])
    user_type = models.CharField(max_length=1,choices=TYPE_CHOICES,default='B')
    boss_id = models.ForeignKey(
        'self', default=None,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='visitors'
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True) 
    #for visitors  
    center_x = models.FloatField(null=True,blank=True)
    center_y = models.FloatField(null=True,blank=True)
    radius = models.FloatField(null=True,blank=True)                            

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts' 

    USERNAME_FIELD = 'email'
    objects = CustomUserManger()    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin 

    def __str__(self):
	    return f"{self.email}"    


class Company(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    image = models.ImageField(upload_to=company_image_path,null=True,blank=True)
    category = models.ForeignKey(
		Category,
		on_delete=models.SET_NULL,
		null=True,
		related_name='companies'
	)
    boss_id = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies' 

    def __str__(self):
	    return f'{self.name}' 


class Activity(models.Model):
    hours_of_work = models.FloatField(null=True,blank=True,default=0)
    sales_amount = models.FloatField(null=True,blank=True,default=0)
    num_out_of_limit = models.IntegerField(null=True,blank=True,default=0)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='creator',null=True)
    visitor_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='assignee',null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities' 

    def __str__(self):
	    return f'{self.visitor_id}-{self.create_at}'       
        
    



    

