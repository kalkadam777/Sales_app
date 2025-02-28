from .models import Order, Transaction
from .serializers import OrderSerializer, TransactionSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Создание заказа и автоматическое создание транзакции"""
        with transaction.atomic():
            order = serializer.save(user=self.request.user)

            # Проверяем, достаточно ли средств у пользователя
            if order.order_type == "buy" and order.user.balance < order.total_price:
                return Response(
                    {"error": "Недостаточно средств"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Обновляем баланс пользователя
            if order.order_type == "buy":
                order.user.balance -= order.total_price
            else:  # sell
                order.user.balance += order.total_price
            order.user.save()

            # Создаем транзакцию
            Transaction.objects.create(
                user=order.user,
                order=order,
                amount=order.total_price,
                transaction_type="debit" if order.order_type == "buy" else "credit"
            )

            order.status = "completed"
            order.save()

            return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)



class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Выдаем только транзакции пользователя"""
        return Transaction.objects.filter(order__user=self.request.user)
