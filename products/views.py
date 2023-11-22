from django.shortcuts import render
from .models import Guide


def products_guides(request):
    """ A view to show all workout guides """

    guides = Guide.objects.all()

    context = {
        'guides': guides,
    }

    return render(request, "products/products.html", context)
