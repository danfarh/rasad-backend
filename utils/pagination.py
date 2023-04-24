from django.conf import settings
from rest_framework.pagination import PageNumberPagination

#pagination
class SetPagination(PageNumberPagination):
	page_size = settings.PRODUCTS_PAGINATION
	page_size_query_param = 'page_size'
	max_page_size = settings.MAX_PRODUCTS_PAGINATION