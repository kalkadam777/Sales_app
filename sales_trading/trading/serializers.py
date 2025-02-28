from rest_framework import serializers
from .models import Order, Transaction

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    def validate(self, data):
        """Проверяем, что цена заказа положительная"""
        if data['total_price'] <= 0:
            raise serializers.ValidationError("Цена должна быть положительной")
        return data


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
