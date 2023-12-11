from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Guide
from django.contrib import messages


def view_cart(request):
    """ A view to show the shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.add_message(request, messages.SUCCESS,
                             f'Item {item_id} was added to you cart')
    else:
        cart[item_id] = quantity
        messages.add_message(request, messages.SUCCESS,
                             f'Item {item_id} was added to you cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """remove an item from the shopping cart"""

    try:
        cart = request.session.get('cart', {})

        if item_id in cart:
            cart.pop(item_id)
            messages.add_message(request, messages.ERROR,
                         'Your item has been deleted from the cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
