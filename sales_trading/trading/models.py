from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Order(models.Model):
    BUY = 'buy'
    SELL = 'sell'
    ORDER_TYPES = [(BUY, 'Buy'), (SELL, 'Sell')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=4, choices=ORDER_TYPES)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.order_type} {self.quantity} {self.product} at {self.price}"


class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=[("credit", "Credit"), ("debit", "Debit")])
    executed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[("pending", "Pending"), ("completed", "Completed")])


    def __str__(self):
        return f"Transaction for {self.order} at {self.executed_at}"
