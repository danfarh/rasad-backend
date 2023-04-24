from .models import Category
from rest_framework import generics
from .serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class ListCompanyCategoriesView(generics.ListAPIView): 
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer 

    def get_queryset(self):
        """
        get params
        C -> company
        P -> Product
        """
        type = self.request.GET.get('type')
        category = Category.objects.filter(type=type)
        return category
