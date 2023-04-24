from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.admin.sites import AdminSite
from django.conf import settings
from django.conf.urls.static import static
from utils.initDB import initDB
#simple jwt
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
#swagger
from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
	path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('initdb/', initDB, name='init_db'),
    path('', include('users.urls')),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('comment/', include('comment.urls')),
    path('', include('Job.urls')),

    #swagger urls
   	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG == True:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


AdminSite.site_header = 'Administration'
AdminSite.index_title = 'Rasad'
AdminSite.site_title = 'Rasad Admin' 