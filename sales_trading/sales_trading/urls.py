from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from .swagger_urls import urlpatterns as swagger_urls
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users import views
from payments.views import CreateCheckoutSessionView, payment_success, payment_cancel, stripe_webhook
from django.contrib.auth.views import LogoutView, PasswordChangeView,PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    
    # DRF
    path('api/drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('sales/', include('sales.urls')),
    path('trading/', include('trading.urls')),
    path('analytics/', include('analytics.urls')),
    
    path("webhook/stripe/", stripe_webhook, name="stripe_webhook"),
    path("payment/success/", payment_success, name="payment_success"),
    path("payment/cancel/", payment_cancel, name="payment_cancel"),
    path('create-checkout-session/<int:order_id>/<int:amount>/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),

    
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    # path("users/", include("users.urls")),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    
    path('password_change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html',
        email_template_name='users/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done')
        ), 
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    
    path('password-reset/<uidb64>/<token>/', 
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
                success_url=reverse_lazy('password_reset_complete')
             ), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    
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
