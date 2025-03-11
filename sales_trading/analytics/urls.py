from django.urls import path
from analytics.views import SalesReportView
from .views import analytics_dashboard

urlpatterns = [
    path("sales-report/", SalesReportView.as_view(), name="sales-report"),
    path('', analytics_dashboard, name='analytics_dashboard'),
]