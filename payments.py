import stripe
import os

stripe.api_key = os.getenv("STRIPE_KEY")

def criar_checkout():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": "price_1TNxcaGVW8FRd5MmDxnsXeU9",
            "quantity": 1,
        }],
        mode="subscription",
        success_url="http://localhost:3000/sucesso",
        cancel_url="http://localhost:3000/cancelado",
    )

    return session.url
