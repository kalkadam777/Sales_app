from django.urls import path
from analytics.views import SalesReportView

urlpatterns = [
    path("sales-report/", SalesReportView.as_view(), name="sales-report"),
]