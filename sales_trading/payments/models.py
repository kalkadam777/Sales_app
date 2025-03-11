from django.db import models

class Payment(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField(help_text="Сумма в копейках (100 = 1.00 KZT)")
    currency = models.CharField(max_length=3, default="kzt")
    stripe_payment_intent = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Ожидание'), ('paid', 'Оплачен'), ('failed', 'Ошибка')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Оплата {self.order_id} - {self.status}"
