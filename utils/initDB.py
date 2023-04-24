from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from users.models import CustomUser as User,Company,Activity
from category.models import Category


def initDB(request):
    #delete all tabels
    User.objects.all().delete()
    Category.objects.all().delete()
    Company.objects.all().delete()
    Activity.objects.all().delete()
    
    #super user
    super_user = User(
        email='admin@gmail.com',
        password=make_password('admin'),
    )
    super_user.is_admin = True
    super_user.is_superuser = True
    super_user.save()
    
    #boss
    boss = User(
        first_name = 'boss1',
        last_name = 'boss',
        phone_number= '09373538500',
        email='boss1@gmail.com',
        password=make_password('bosspassword'),
        user_type='B'
    )
    boss.save()

    #customer
    customer = User(
        first_name = 'customer1',
        last_name = 'customer',
        phone_number= '09373538501',
        email='customer1@gmail.com',
        password=make_password('customerpassword'),
        user_type='C'
    )
    customer.save()

    #visitors
    visitor1 = User(
        first_name = 'visitor1',
        last_name = 'visitor1',
        phone_number= '09123538501',
        email='visitor1@gmail.com',
        password=make_password('visitor1password'),
        user_type='V',
        boss_id=boss,
        center_x= 1000,
        center_y= 5000,
        radius=500
    )
    visitor1.save()
    visitor2 = User(
        first_name = 'visitor2',
        last_name = 'visitor2',
        phone_number= '09123538502',
        email='visitor2@gmail.com',
        password=make_password('visitor2password'),
        user_type='V',
        boss_id=boss,
        center_x= 2000,
        center_y= 5000,
        radius=500
    )
    visitor2.save()
    visitor3 = User(
        first_name = 'visitor3',
        last_name = 'visitor3',
        phone_number= '09123538503',
        email='visitor3@gmail.com',
        password=make_password('visitor3password'),
        user_type='V',
        boss_id=boss,
        center_x= 3000,
        center_y=4800,
        radius=500
    )
    visitor3.save()
    print('seed users...')
    
    #categories
    Category.objects.create(title='Mobile', slug='Mobile', type='P')
    Category.objects.create(title='Laptop' ,slug='Laptop', type='P')
    Category.objects.create(title='Tablet' ,slug='Tablet', type='P')
    Category.objects.create(title='PC' ,slug='PC', type='P')
    Category.objects.create(title='Camera' ,slug='Camera', type='P')
    Category.objects.create(title='Fashion And Clothing' ,slug='Fashion And Clothing', type='P')
    Category.objects.create(title='Shoe' ,slug='Shoe', type='P')
    Category.objects.create(title='Shirt' ,slug='Shirt', type='P')
    Category.objects.create(title='Hat' ,slug='Hat', type='P')
    Category.objects.create(title='Sport' ,slug='Sport', type='P')
    Category.objects.create(title='Accessory' ,slug='Accessory', type='P')
    Category.objects.create(title='Super Market' ,slug='Super Market', type='P')
    Category.objects.create(title='Stationery' ,slug='Stationery', type='P')

    category1 = Category.objects.create(title='Digital Product Store' , slug='Digital Product Store', type='C')
    Category.objects.create(title='Boutique' , slug='Boutique', type='C')
    Category.objects.create(title='Super Market' , slug='Super Markett', type='C')
    Category.objects.create(title='Restaurant' , slug='Restaurant', type='C')
    Category.objects.create(title='Car Exhibition' , slug='Car Exhibition', type='C')
    Category.objects.create(title='Stationery Store' , slug='Stationery Store', type='C')
    Category.objects.create(title='Cellphone Shop' , slug='Cellphone Shop', type='C')
    Category.objects.create(title='Toy Shop' , slug='Toy Shop', type='C')
    Category.objects.create(title='Cosmetic Store' , slug='Cosmetic Store', type='C')
    print('seed categories...')

    #company
    company1 = Company.objects.create(name='company1',boss_id=boss,category=category1)
    print('seed company...')

    #activities
    Activity.objects.create(hours_of_work=6,sales_amount=500000,num_out_of_limit=1,company_id=company1,visitor_id=visitor1)
    Activity.objects.create(hours_of_work=8,sales_amount=800000,num_out_of_limit=0,company_id=company1,visitor_id=visitor1)
    Activity.objects.create(hours_of_work=9,sales_amount=900000,num_out_of_limit=0,company_id=company1,visitor_id=visitor1)
    Activity.objects.create(hours_of_work=7,sales_amount=700000,num_out_of_limit=0,company_id=company1,visitor_id=visitor1)
    Activity.objects.create(hours_of_work=10,sales_amount=600000,num_out_of_limit=1,company_id=company1,visitor_id=visitor1)

    Activity.objects.create(hours_of_work=6,sales_amount=900000,num_out_of_limit=1,company_id=company1,visitor_id=visitor2)
    Activity.objects.create(hours_of_work=8,sales_amount=800000,num_out_of_limit=2,company_id=company1,visitor_id=visitor2)
    Activity.objects.create(hours_of_work=9,sales_amount=900000,num_out_of_limit=0,company_id=company1,visitor_id=visitor2)
    Activity.objects.create(hours_of_work=7,sales_amount=700000,num_out_of_limit=1,company_id=company1,visitor_id=visitor2)
    Activity.objects.create(hours_of_work=10,sales_amount=800000,num_out_of_limit=1,company_id=company1,visitor_id=visitor2)

    Activity.objects.create(hours_of_work=6,sales_amount=1000000,num_out_of_limit=1,company_id=company1,visitor_id=visitor3)
    Activity.objects.create(hours_of_work=8,sales_amount=800000,num_out_of_limit=1,company_id=company1,visitor_id=visitor3)
    Activity.objects.create(hours_of_work=9,sales_amount=900000,num_out_of_limit=0,company_id=company1,visitor_id=visitor3)
    Activity.objects.create(hours_of_work=7,sales_amount=700000,num_out_of_limit=0,company_id=company1,visitor_id=visitor3)
    Activity.objects.create(hours_of_work=10,sales_amount=950000,num_out_of_limit=1,company_id=company1,visitor_id=visitor3)
    print('seed activities...')

    print('seed all models')
    return HttpResponse("init successfully")    