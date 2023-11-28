from django.shortcuts import render, get_object_or_404
from .models import Guide


def products_guides(request):
    """ A view to show all workout guides """

    guides = Guide.objects.all()

    context = {
        'guides': guides,
    }

    return render(request, "products/products.html", context)


def product_guide_detail(request, guide_id):
    """ A view to show each guide's details"""

    guide = get_object_or_404(Guide, pk=guide_id)

    context = {
        'guide': guide,
    }

    return render(request, "products/product_guide_detail.html", context)
