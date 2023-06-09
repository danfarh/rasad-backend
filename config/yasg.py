#swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#create schema for swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Rasad API",
        default_version='v1',
        description="All of the endpoints.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@site.local"),
        license=openapi.License(name="GPLv3 License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)