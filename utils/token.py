import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    access_token.set_exp(lifetime=timedelta(days=10))

    return {
        'refresh': str(refresh),
        'access': str(access_token),
    }

# def generateToken(user):
#     JWT_SECRET = settings.SECRET_KEY
#     JWT_ALGORITHM = 'HS256'
#     JWT_EXP_DELTA_SECONDS = 20
#     payload = {
#         'email': user.email,
#         'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#     return token