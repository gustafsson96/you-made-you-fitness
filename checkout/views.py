from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products_guides'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O4QqsJ3bX1eIb24JUAlNmcSX4Z6gEvWBGD96PVPQi00LFuyqFxtvEafIhjnK1c9tqCO8QPwClKFWwffn29efvBd00P5swrlGv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
