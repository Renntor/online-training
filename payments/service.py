import stripe
import os


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

    paymentlink = stripe.PaymentLink.create(
        line_items=[{"price": starter_subscription_price['id'], "quantity": 1}]
    )
    return paymentlink['url']

# def payment_verification(payment_id):
#     """
#     Проверка платежа в сервисе stripe
#     """
#     stripe.api_key = os.getenv('STRIPE_API_KEY')
#
#     s = stripe.PaymentLink.retrieve(
#         payment_id,
#     )
#     print(s)