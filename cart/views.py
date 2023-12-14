from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Guide
from django.contrib import messages


def view_cart(request):
    """ view to show the shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in cart:
        messages.add_message(request, messages.ERROR,
                         'This item is already in your shopping cart')
    else:
        cart[item_id] = quantity
        messages.add_message(request, messages.SUCCESS,
                             'The item was added to your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """remove an item from the shopping cart"""

    try:
        cart = request.session.get('cart', {})

        if item_id in cart:
            cart.pop(item_id)
            messages.add_message(request, messages.INFO,
                        'Your item has been deleted from the shopping cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
