from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .swagger_urls import urlpatterns as swagger_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    
    # DRF
    path('api/drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # API
    path('api/users/', include('users.urls')),
    path("api/analytics/", include("analytics.urls")),
    path('api/products/', include('products.urls')),
    path('api/trading/', include('trading.urls')),
    
    # JWT-токены
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + swagger_urls  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
