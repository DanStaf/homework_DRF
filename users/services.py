import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):

    title = f"{instance.course}" if instance.course else f"{instance.lesson}"
    return stripe.Product.create(name=title)


def create_stripe_price(product, amount):

    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product=product.get("id")
    )


def create_stripe_session(price, success_url):

    return stripe.checkout.Session.create(
        success_url=success_url,
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )


def get_stripe_session_retrieve(session_id):

    response = stripe.checkout.Session.retrieve(session_id, )
    return response.get("status")
