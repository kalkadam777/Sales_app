from django.urls import path
from .views import CreateCheckoutSessionView, payment_success, payment_cancel, stripe_webhook


# urlpatterns = [
#     path("webhook/stripe/", stripe_webhook, name="stripe_webhook"),
#     path("payment/success/", payment_success, name="payment_success"),
#     path("payment/cancel/", payment_cancel, name="payment_cancel"),
#     path('create-checkout-session/<int:order_id>/<int:amount>/', CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
# ]

