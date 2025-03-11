import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import Payment
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        order_id = "order_" + str(kwargs["order_id"])  # Пример заказа
        amount = kwargs["amount"] * 100  # Конвертация в копейки
        currency = "kzt"

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': currency,
                        'product_data': {'name': f"Заказ {order_id}"},
                        'unit_amount': amount,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url="http://127.0.0.1:8000/payment/success/",
                cancel_url="http://127.0.0.1:8000/payment/cancel/",
            )

            # Создание записи платежа
            payment = Payment.objects.create(
                order_id=order_id,
                amount=amount,
                stripe_payment_intent=session.payment_intent,
                status="pending"
            )

            return JsonResponse({'id': session.id})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def payment_success(request):
    return render(request, "payments/success.html")

def payment_cancel(request):
    return render(request, "payments/cancel.html")


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = json.loads(payload)
    except json.JSONDecodeError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        payment = Payment.objects.get(stripe_payment_intent=session['payment_intent'])
        payment.status = "paid"
        payment.save()

    return HttpResponse(status=200)
