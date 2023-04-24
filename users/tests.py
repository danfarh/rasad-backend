from rest_framework.test import APITestCase
from users.models import CustomUser as User


class UserTestCase(APITestCase):
    def setUp(self):
        boss = User(
            first_name='boss',
            last_name='boss',
            phone_number='09373538508',
            email='boss@gmail.com',
            user_type='B'
        )
        boss.set_password('bosspassword')
        boss.save()

        visitor = User(
            first_name='visitor',
            last_name='visitor',
            phone_number='09373538507',
            email='visitor@gmail.com',
            user_type='V'
        )
        visitor.set_password('visitorpassword')
        visitor.save()
    
    def test_boss_register(self):
        data = {
            'first_name': 'boss2',
            'last_name': 'boss2',
            'phone_number': '09389505414',
            'email': 'boss2@gmail.com',
            'password': 'bosspassword',
            'user_type':'B'
        }
        response = self.client.post('/register/', data, format='json') 
        self.assertEqual(response.status_code, 201)

    def test_boss_login(self):
        data = {
            'phone_number': '09373538508',
            'password': 'bosspassword'
        }
        response = self.client.post('/login/', data, format='json') 
        self.assertEqual(response.status_code, 200)   
        
    def test_visitor_register(self):
        data = {
            'first_name': 'visitor2',
            'last_name': 'visitor2',
            'phone_number': '09127029695',
            'email': 'visitor2@gmail.com',
            'password': 'visitorpassword',
            'user_type':'V'
        }
        response = self.client.post('/register/', data, format='json') 
        self.assertEqual(response.status_code, 201) 

    def test_visitor_login(self):
        data = {
            'phone_number': '09373538507',
            'password': 'visitorpassword'
        }
        response = self.client.post('/login/', data, format='json') 
        self.assertEqual(response.status_code, 200)        
    


