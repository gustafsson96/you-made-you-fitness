from django.shortcuts import render, redirect


def view_cart(request):
    """A view to show the shopping cart page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def delete_item(request, item_id):
    """ Delete a product from the shopping cart """

    item_id.delete()

    return redirect(redirect_url)
