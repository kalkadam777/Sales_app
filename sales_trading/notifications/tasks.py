from celery import shared_task

@shared_task
def send_trade_notification(order_id, amount, status):
    print(f"Notification sent: Order {order_id}, Amount: {amount}, Status: {status}")
