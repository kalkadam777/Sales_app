from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, TransactionViewSet
from .views import trading_dashboard

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('site/', trading_dashboard, name='trading_dashboard'),
]
