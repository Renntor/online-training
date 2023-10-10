import os

import stripe


class CreateMixin:
    def perform_create(self, serializer):
        new_object = serializer.save()
        new_object.owner = self.request.user
        new_object.save()


def create_payment(title: str, price: float):
    """
    Создание продукта в сервисе stripe
    """

    stripe.api_key = os.getenv('STRIPE_API_KEY')

    starter_subscription = stripe.Product.create(
        name=title,
        description=f"${price}",
    )

    starter_subscription_price = stripe.Price.create(
        unit_amount=price * 100,
        currency="usd",
        product=starter_subscription['id'],
    )

    stripe.PaymentLink.create(
        line_items=[{"price": starter_subscription_price['id'], "quantity": 1}]
    )


def payment_verification(payment_id):
    """
    Проверка платежа в сервисе stripe
    """
    stripe.PaymentIntent.retrieve(
        payment_id,
    )
