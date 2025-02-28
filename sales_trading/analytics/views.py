from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, Avg
from trading.models import Order

class SalesReportView(APIView):
    def get(self, request):
        total_sales = Order.objects.filter(transactions__status="completed").aggregate(Sum("transactions__amount"))["transactions__amount__sum"] or 0
        completed_orders = Order.objects.filter(transactions__status="completed").distinct().count()
        avg_order_value = Order.objects.filter(transactions__status="completed").aggregate(Avg("transactions__amount"))["transactions__amount__avg"] or 0

        data = {
            "total_sales": total_sales,
            "completed_orders": completed_orders,
            "avg_order_value": avg_order_value,
        }
        return Response(data)
