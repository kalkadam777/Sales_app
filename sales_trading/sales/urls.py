from django.urls import path
from .views import sales_dashboard

urlpatterns = [
    path('', sales_dashboard, name='sales_dashboard'),
]
