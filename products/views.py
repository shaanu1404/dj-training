from django.shortcuts import render
from .models import Product


def all_products_view(request):
    all_products = Product.objects.all()
    return render(request, 'products/list.html', {"all_products": all_products})


def single_product_view(request, id):
    product = None
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        print("Product does not exist")

    context = {
        "product": product
    }
    return render(request, 'products/detail.html', context)
